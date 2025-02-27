def find_second_smallest_num(num_list):
    if len(num_list) < 201:
        return None
    slice_list = sorted(num_list[50:201])
    if len(slice_list) < 2:
        return None
    return slice_list[1]