def find_second_smallest_num(numbers):
    if len(numbers) < 47:
        return None
    subset = numbers[36:47]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset))
    return unique_subset[1] if len(unique_subset) >= 2 else None