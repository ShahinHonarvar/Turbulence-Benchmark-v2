def find_second_largest_num(num_list):
    if len(num_list) < 10:
        return None
    else:
        slice_list = num_list[8:10]
        sorted_slice_list = sorted(slice_list, reverse=True)
        if len(sorted_slice_list) < 2:
            return None
        else:
            return sorted_slice_list[1]