def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 246:
        return None
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None