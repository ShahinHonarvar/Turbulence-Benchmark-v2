def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 6:
        return None
    first_largest = max(numbers[:6])
    second_largest = None
    for num in numbers[6:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest