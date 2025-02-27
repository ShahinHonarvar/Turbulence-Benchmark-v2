def find_second_largest_num(num_list):
    slice_list = num_list[27:56]
    if len(slice_list) < 2:
        return None
    first_max = max(slice_list)
    slice_list.remove(first_max)
    if slice_list:
        return max(slice_list)
    else:
        return None