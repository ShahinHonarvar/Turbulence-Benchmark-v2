def find_second_smallest_num(numbers):
    if len(numbers) <= 31:
        return None
    slice_range = numbers[30:88]
    if len(slice_range) == 0:
        return None
    sorted_slice = sorted(slice_range)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None