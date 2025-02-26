def find_second_largest_num(numbers):
    if len(numbers) < 76:
        return None
    slice_range = numbers[74:96]
    if not slice_range:
        return None
    sorted_slice = sorted(set(slice_range), reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None