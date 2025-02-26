def find_second_largest_num(numbers):
    if len(numbers) <= 11:
        return None
    slice_subset = numbers[10:101]
    if not slice_subset:
        return None
    sorted_subset = sorted(set(slice_subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None