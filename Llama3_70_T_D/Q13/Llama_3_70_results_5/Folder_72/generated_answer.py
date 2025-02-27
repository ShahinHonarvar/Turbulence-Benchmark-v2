def find_second_largest_num(num_list):
    if 29 > len(num_list) - 1 or 51 > len(num_list) - 1:
        return None
    slice_list = num_list[29:52]
    slice_list.sort(reverse=True)
    if len(slice_list) < 2:
        return None
    return slice_list[1]