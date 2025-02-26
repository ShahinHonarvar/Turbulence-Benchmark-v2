def find_second_largest_num(numbers):
    if len(numbers) <= 56:
        return None
    slice_range = numbers[56:99]
    if len(slice_range) < 2:
        return None
    slice_range = sorted(slice_range, reverse=True)
    return slice_range[1]