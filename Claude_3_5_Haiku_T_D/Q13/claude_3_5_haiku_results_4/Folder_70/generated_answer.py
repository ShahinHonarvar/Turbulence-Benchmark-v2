def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    slice_subset = numbers[28:33]
    if len(slice_subset) == 0:
        return None
    sorted_slice = sorted(slice_subset, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None