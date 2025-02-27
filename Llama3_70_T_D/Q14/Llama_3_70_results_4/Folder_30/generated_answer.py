def find_second_smallest_num(num_list):
    slice_list = sorted(num_list[26:53])
    if len(slice_list) < 2:
        return None
    return slice_list[1]