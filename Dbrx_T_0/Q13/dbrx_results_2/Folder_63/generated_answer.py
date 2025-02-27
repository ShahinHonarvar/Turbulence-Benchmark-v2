def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 89 - 22 + 1:
        return None
    second_largest = None
    largest = max(numbers[22:89])
    for num in numbers[22:89]:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest