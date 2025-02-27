def find_second_largest_num(num_list):
    if len(num_list) < 52:
        return None
    sliced_list = num_list[15:52]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]