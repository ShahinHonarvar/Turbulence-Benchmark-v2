def find_second_smallest_num(numbers):
    if len(numbers) <= 37:
        return None
    slice_range = numbers[37:77]
    if not slice_range:
        return None
    sorted_slice = sorted(set(slice_range))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None