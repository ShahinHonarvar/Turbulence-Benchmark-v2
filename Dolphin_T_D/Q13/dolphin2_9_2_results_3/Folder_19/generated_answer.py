def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[3:6]
    largest = max(numbers)
    second_largest = None
    for number in numbers:
        if number != largest and (second_largest is None or number > second_largest):
            second_largest = number
    return second_largest