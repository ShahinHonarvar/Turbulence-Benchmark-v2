def find_second_largest_num(num_list):
    if len(num_list) < 52:
        return None
    slice_list = num_list[29:52]
    if len(set(slice_list)) < 2:
        return None
    second_largest = sorted(set(slice_list), reverse=True)[1]
    return second_largest