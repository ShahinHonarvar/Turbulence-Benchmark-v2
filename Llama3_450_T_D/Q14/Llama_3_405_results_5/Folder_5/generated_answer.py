def find_second_smallest_num(num_list):
    if len(num_list) < 6:
        return None
    slice_list = num_list[3:6]
    slice_list.sort()
    if len(slice_list) < 2:
        return None
    return slice_list[1]