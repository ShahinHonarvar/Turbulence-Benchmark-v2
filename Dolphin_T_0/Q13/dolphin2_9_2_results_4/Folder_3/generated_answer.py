def find_second_largest_num(num_list):
    slice_list = num_list[62:93]
    if len(slice_list) < 2:
        return None
    else:
        sorted_slice = sorted(slice_list)
        return sorted_slice[-2]