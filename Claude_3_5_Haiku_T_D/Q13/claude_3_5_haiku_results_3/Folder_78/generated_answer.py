def find_second_largest_num(numbers):
    if len(numbers) <= 43:
        return None
    slice_list = numbers[43:52]
    if len(slice_list) == 0:
        return None
    sorted_slice = sorted(set(slice_list), reverse=True)
    return sorted_slice[1] if len(sorted_slice) >= 2 else None