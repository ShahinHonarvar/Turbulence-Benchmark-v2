def find_second_largest_num(num_list):
    slice_list = num_list[28:33]
    if len(slice_list) < 2:
        return None
    else:
        slice_list.sort(reverse=True)
        return slice_list[1]