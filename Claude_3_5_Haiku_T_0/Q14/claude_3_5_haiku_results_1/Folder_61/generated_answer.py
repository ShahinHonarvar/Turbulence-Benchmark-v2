def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 8:
        return None
    subset = numbers[:8]
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) > 1 else None