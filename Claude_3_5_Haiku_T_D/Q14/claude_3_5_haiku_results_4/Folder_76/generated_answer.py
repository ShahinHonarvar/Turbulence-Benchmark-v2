def find_second_smallest_num(numbers):
    if len(numbers) <= 533:
        return None
    subset = numbers[533:606]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) > 1 else None