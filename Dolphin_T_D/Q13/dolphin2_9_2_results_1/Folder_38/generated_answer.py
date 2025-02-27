def find_second_largest_num(my_list):
    slice_list = my_list[22:64]
    if len(slice_list) < 2:
        return None
    else:
        slice_list.sort()
        return slice_list[-2]