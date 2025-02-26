def find_second_largest_num(numbers):
    if len(numbers) < 102:
        return None
    slice_range = numbers[100:201]
    if len(slice_range) == 0:
        return None
    sorted_slice = sorted(slice_range, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None