def find_second_smallest_num(numbers):
    if len(numbers) <= 31:
        return None
    slice_range = numbers[31:73]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(slice_range)
    return sorted_slice[1]