def find_second_largest_num(numbers):
    if len(numbers) < 32 or len(numbers) <= 48:
        return None
    subset = numbers[30:49]
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]