def find_second_largest_num(numbers):
    if len(numbers) <= 20:
        return None
    slice_range = numbers[20:201]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(slice_range, reverse=True)
    return sorted_slice[1]