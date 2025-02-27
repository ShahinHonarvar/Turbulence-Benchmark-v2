def find_second_smallest_num(num_list):
    if 10 < len(num_list) - 1:
        slice_list = num_list[10:11]
        slice_list.sort()
        if len(slice_list) > 1:
            return slice_list[1]
    return None