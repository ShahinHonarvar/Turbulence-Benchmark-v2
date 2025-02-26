def find_second_smallest_num(numbers):
    if len(numbers) <= 61:
        return None
    subset = numbers[60:201]
    if not subset:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None