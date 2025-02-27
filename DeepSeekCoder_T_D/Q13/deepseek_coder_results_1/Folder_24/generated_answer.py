def find_second_largest_num(num_list):
    if len(num_list) < 96:
        return None
    sub_list = num_list[74:96]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]