def find_second_smallest_num(numbers):
    if len(numbers) <= 23:
        return None
    slice_list = numbers[23:24]
    if len(slice_list) == 0:
        return None
    return slice_list[0]