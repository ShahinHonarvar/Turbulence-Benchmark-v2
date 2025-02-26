def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    slice_range = numbers[55:99]
    if not slice_range:
        return None
    sorted_slice = sorted(set(slice_range))
    return sorted_slice[1] if len(sorted_slice) > 1 else None