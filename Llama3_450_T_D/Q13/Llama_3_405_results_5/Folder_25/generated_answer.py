def find_second_largest_num(num_list):
    if len(num_list) < 93 or 29 > len(num_list):
        return None
    sliced_list = sorted(num_list[29:94])
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]