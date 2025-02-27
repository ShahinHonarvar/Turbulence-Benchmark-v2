def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 68 - 13 + 1:
        return None
    second_largest = None
    largest = max(numbers[13:68])
    for num in numbers[13:68]:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest