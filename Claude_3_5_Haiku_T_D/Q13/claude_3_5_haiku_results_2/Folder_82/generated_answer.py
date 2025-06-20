def find_second_largest_num(numbers):
    if len(numbers) <= 21:
        return None
    slice_range = numbers[20:201]
    if len(slice_range) == 0:
        return None
    sorted_slice = sorted(slice_range, reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None