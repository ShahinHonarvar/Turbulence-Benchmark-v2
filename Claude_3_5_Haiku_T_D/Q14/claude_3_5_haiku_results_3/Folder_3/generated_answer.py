def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    slice_range = numbers[27:56]
    if len(slice_range) == 0:
        return None
    sorted_slice = sorted(set(slice_range))
    return sorted_slice[1] if len(sorted_slice) > 1 else None