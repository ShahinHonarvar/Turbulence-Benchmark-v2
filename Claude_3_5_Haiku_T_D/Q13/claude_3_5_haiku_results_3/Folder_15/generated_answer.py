def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:4]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest