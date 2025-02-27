def find_second_largest_num(num_list):
    if len(num_list) < 746 or len(num_list) < 263:
        return None
    sliced_list = num_list[262:747]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]