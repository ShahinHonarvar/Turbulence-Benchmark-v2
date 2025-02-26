def find_second_largest_num(numbers):
    if len(numbers) <= 22:
        return None
    subset = numbers[22:89]
    if len(subset) <= 1:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]