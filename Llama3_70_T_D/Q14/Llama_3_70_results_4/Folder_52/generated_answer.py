def find_second_smallest_num(num_list):
    slice_list = num_list[64:67]
    if len(slice_list) < 2:
        return None
    return sorted(set(slice_list))[1]