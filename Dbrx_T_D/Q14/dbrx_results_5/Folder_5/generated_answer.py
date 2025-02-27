def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    slice_set = set(numbers[3:6])
    if len(slice_set) < 2:
        return None
    slice_list = sorted(slice_set)
    return slice_list[1]