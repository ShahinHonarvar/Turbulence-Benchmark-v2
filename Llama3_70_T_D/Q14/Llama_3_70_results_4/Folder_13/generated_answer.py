def find_second_smallest_num(num_list):
    if len(num_list) < 33:
        return None
    slice_list = num_list[28:33]
    if len(slice_list) < 2:
        return None
    slice_list.sort()
    return slice_list[1]