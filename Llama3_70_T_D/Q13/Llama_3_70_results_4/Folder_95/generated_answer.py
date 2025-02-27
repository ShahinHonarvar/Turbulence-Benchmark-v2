def find_second_largest_num(num_list):
    slice_list = num_list[82:87]
    if len(slice_list) >= 2:
        slice_list.sort(reverse=True)
        return slice_list[1]
    else:
        return None