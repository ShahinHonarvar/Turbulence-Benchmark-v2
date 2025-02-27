def find_second_largest_num(num_list):
    if len(num_list) < 67:
        return None
    sub_list = sorted(num_list[64:67])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]