def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 90 < 2:
        return None
    first_largest = max(numbers[:91])
    second_largest = None
    for num in numbers[90:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest