def find_second_smallest_num(num_list):
    slice_list = sorted(num_list[32:36])
    if len(slice_list) > 1:
        return slice_list[1]
    else:
        return None