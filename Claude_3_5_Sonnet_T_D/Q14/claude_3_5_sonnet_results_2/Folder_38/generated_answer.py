def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    subset = numbers[37:52]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1] if len(sorted_subset) > 1 else None