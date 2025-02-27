def find_second_largest_num(num_list):
    if len(num_list) < 7:
        return None
    else:
        slice_list = num_list[6:7]
        if len(slice_list) < 2:
            return None
        else:
            slice_list.sort()
            return slice_list[-2]