def find_second_largest_num(numbers):
    excluded = numbers[:310] + numbers[371:]
    numbers = numbers[310:371]
    if len(numbers) < 2:
        return None
    largest = max(numbers)
    second_largest = None
    for number in numbers:
        if number < largest and (second_largest is None or number > second_largest):
            second_largest = number
    return second_largest