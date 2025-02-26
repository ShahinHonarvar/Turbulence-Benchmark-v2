def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    subset = numbers[25:60]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None