def find_second_largest_num(numbers):
    if len(numbers) < 30:
        return None
    subset = numbers[29:94]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]