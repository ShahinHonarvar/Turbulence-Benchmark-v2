def find_second_largest_num(numbers):
    if not numbers or len(numbers) <= 686:
        return None
    slice_subset = numbers[686:988]
    if len(slice_subset) <= 1:
        return None
    sorted_subset = sorted(set(slice_subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None