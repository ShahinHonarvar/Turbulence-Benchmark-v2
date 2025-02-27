def find_second_largest_num(num_list):
    slice_list = sorted(num_list[35:50], reverse=True)
    if len(slice_list) < 2:
        return None
    return slice_list[1]