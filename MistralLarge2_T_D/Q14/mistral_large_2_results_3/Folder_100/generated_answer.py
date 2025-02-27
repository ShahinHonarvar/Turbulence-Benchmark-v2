def find_second_smallest_num(numbers):
    subset = [num for i, num in enumerate(numbers) if 43 <= i <= 51]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    unique_subset.sort()
    return unique_subset[1] if len(unique_subset) > 1 else None