def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    slice_subset = numbers[36:47]
    if len(slice_subset) == 0:
        return None
    sorted_subset = sorted(slice_subset, reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]