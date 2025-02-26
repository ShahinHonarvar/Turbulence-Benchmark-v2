def find_second_smallest_num(numbers):
    if len(numbers) <= 60:
        return None
    slice_range = numbers[60:201]
    if len(slice_range) == 0:
        return None
    sorted_slice = sorted(set(slice_range))
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]