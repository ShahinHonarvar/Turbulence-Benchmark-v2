def find_second_smallest_num(numbers):
    if len(numbers) < 748:
        return None
    subset = numbers[262:747]
    if len(subset) < 2:
        return None
    subset_sorted = sorted(set(subset))
    return subset_sorted[1] if len(subset_sorted) >= 2 else None