def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 640:
        return None
    subset = numbers[639:976]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest