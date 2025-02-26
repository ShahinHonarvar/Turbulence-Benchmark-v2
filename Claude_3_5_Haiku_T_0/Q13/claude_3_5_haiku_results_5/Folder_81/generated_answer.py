def find_second_largest_num(numbers):
    if len(numbers) < 11:
        return None
    slice_range = numbers[10:101]
    if len(slice_range) == 0:
        return None
    sorted_slice = sorted(set(slice_range), reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None