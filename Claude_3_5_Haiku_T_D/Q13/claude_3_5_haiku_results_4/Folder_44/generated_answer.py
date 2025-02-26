def find_second_largest_num(numbers):
    if len(numbers) <= 14:
        return None
    subset = numbers[13:69]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    second_largest = None
    for num in subset:
        if num > second_largest and num < first_largest:
            second_largest = num
    return second_largest