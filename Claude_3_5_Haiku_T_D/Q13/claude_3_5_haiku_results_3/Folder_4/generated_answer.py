def find_second_largest_num(numbers):
    if len(numbers) <= 92 or len(numbers) < 13:
        return None
    subset = numbers[12:93]
    if len(subset) <= 1:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest