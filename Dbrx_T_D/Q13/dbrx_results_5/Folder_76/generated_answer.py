def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers_in_range = numbers[686:988]
    if len(numbers_in_range) < 2:
        return None
    first, second = (max(numbers_in_range), None)
    for num in numbers_in_range:
        if num < first and (num > second or second is None):
            second = num
    return second