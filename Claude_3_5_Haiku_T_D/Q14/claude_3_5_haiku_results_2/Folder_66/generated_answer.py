def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    slice_range = numbers[62:100]
    if not slice_range:
        return None
    unique_slice = sorted(set(slice_range))
    if len(unique_slice) < 2:
        return None
    return unique_slice[1]