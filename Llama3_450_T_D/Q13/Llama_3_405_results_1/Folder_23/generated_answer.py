def find_second_largest_num(num_list):
    if len(num_list) < 72:
        return None
    slice_list = num_list[52:72]
    slice_list.sort(reverse=True)
    if len(slice_list) > 1:
        return slice_list[1]
    else:
        return None