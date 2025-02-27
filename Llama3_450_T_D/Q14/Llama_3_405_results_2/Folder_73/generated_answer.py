def find_second_smallest_num(num_list):
    slice_list = num_list[59:98]
    if len(slice_list) < 2:
        return None
    else:
        return sorted(slice_list)[1]