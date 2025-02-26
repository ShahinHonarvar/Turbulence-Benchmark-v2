def find_second_largest_num(numbers):
    if len(numbers) <= 23:
        return None
    slice_list = numbers[23:24]
    if len(slice_list) == 0:
        return None
    return sorted(slice_list, reverse=True)[1] if len(slice_list) > 1 else None