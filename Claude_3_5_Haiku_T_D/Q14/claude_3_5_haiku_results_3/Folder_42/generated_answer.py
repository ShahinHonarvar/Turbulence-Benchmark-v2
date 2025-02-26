def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    subset = numbers[21:98]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None