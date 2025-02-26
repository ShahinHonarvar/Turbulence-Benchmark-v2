def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 663:
        return None
    subset = numbers[661:925]
    if not subset:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None