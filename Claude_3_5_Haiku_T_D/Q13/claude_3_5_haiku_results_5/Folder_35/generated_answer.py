def find_second_largest_num(numbers):
    if len(numbers) < 32 or not 30 <= len(numbers) - 1:
        return None
    slice_range = numbers[30:49]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(slice_range, reverse=True)
    return sorted_slice[1]