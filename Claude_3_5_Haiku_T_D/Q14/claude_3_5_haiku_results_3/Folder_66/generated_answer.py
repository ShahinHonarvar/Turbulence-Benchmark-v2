def find_second_smallest_num(numbers):
    if len(numbers) < 63:
        return None
    slice_subset = numbers[62:100]
    if len(slice_subset) < 2:
        return None
    sorted_subset = sorted(set(slice_subset))
    return sorted_subset[1] if len(sorted_subset) >= 2 else None