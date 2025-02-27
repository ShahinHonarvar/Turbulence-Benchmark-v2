def find_second_largest_num(num_list):
    if len(num_list) < 8:
        return None
    sub_list = num_list[5:8]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]