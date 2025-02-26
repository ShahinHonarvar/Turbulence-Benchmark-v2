def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    slice_subset = numbers[31:73]
    if not slice_subset:
        return None
    sorted_subset = sorted(slice_subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]