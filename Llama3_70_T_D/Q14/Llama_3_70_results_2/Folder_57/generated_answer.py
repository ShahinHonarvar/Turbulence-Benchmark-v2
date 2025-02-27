def find_second_smallest_num(num_list):
    if len(num_list) < 31:
        return None
    slice_list = sorted(num_list[20:31])
    if len(slice_list) < 2:
        return None
    return slice_list[1]