def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) - 56 < 2:
        return None
    first_largest, second_largest = (None, None)
    for num in numbers[56:67]:
        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest