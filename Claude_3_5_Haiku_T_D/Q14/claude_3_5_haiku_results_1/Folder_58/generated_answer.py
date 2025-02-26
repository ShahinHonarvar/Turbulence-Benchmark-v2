def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 310:
        return None
    slice_subset = numbers[310:371]
    if not slice_subset:
        return None
    try:
        sorted_subset = sorted(set(slice_subset))
        return sorted_subset[1] if len(sorted_subset) > 1 else None
    except (TypeError, ValueError):
        return None