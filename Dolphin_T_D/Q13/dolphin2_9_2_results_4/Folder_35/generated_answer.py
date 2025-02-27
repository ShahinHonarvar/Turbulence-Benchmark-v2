def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2:
        return None
    sub_list = num_list[30:49]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]