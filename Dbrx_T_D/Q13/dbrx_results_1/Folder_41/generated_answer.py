def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 7:
        return None
    second_largest = None
    largest = max(numbers[6], key=numbers.index)
    for num in numbers[6:]:
        if num > largest and (second_largest is None or num > second_largest):
            second_largest = num
        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest