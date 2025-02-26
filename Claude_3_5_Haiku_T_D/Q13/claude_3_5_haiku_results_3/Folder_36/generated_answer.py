def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 248:
        return None
    slice_range = numbers[246:751]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(slice_range, reverse=True)
    return sorted_slice[1]