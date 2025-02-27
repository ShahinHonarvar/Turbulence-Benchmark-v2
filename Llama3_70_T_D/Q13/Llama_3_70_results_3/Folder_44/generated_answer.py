def find_second_largest_num(num_list):
    slice_list = num_list[13:69]
    if len(slice_list) < 2:
        return None
    max_num = max(slice_list)
    slice_list.remove(max_num)
    if not slice_list:
        return None
    return max(slice_list)