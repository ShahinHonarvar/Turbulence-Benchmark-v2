def find_second_smallest_num(numbers):
    if len(numbers) < 263:
        return None
    subset = numbers[262:747]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(set(subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]