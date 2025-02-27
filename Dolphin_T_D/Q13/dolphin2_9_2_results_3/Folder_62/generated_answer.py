def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    slice_list = num_list[91:100]
    max_num = max(slice_list)
    slice_list.remove(max_num)
    if len(slice_list) < 2:
        return None
    second_max_num = max(slice_list)
    return second_max_num