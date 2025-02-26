def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    slice_subset = numbers[30:201]
    if len(slice_subset) < 2:
        return None
    sorted_subset = sorted(slice_subset)
    return sorted_subset[1]