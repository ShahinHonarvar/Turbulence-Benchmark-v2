def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    slice_subset = numbers[5:8]
    if len(slice_subset) < 2:
        return None
    sorted_subset = sorted(slice_subset, reverse=True)
    return sorted_subset[1]