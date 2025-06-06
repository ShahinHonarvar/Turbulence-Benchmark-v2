def find_second_smallest_num(numbers):
    if len(numbers) <= 56:
        return None
    slice_range = numbers[56:67]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(set(slice_range))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None