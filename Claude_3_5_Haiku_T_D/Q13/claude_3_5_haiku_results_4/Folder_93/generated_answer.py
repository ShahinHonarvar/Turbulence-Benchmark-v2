def find_second_largest_num(numbers):
    if len(numbers) < 96:
        return None
    slice_range = numbers[75:95]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(set(slice_range), reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None