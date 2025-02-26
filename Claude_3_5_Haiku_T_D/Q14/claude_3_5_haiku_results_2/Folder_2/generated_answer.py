def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 44:
        return None
    slice_list = numbers[43:87]
    if not slice_list:
        return None
    sorted_slice = sorted(set(slice_list))
    return sorted_slice[1] if len(sorted_slice) > 1 else None