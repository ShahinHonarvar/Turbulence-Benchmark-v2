def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    subset = numbers[13:69]
    if not subset:
        return None
    try:
        sorted_subset = sorted(set(subset))
        return sorted_subset[1] if len(sorted_subset) > 1 else None
    except (TypeError, ValueError):
        return None