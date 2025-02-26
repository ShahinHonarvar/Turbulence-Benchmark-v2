def find_second_largest_num(numbers):
    if len(numbers) <= 85:
        return None
    slice_range = numbers[75:86]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(slice_range, reverse=True)
    return sorted_slice[1]