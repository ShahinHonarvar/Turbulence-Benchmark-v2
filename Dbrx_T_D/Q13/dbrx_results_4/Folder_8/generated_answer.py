def find_second_largest_num(numbers):
    numbers_in_range = numbers[23:24]
    if len(numbers_in_range) < 2:
        return None
    first_largest, second_largest = (None, None)
    for num in numbers_in_range:
        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest