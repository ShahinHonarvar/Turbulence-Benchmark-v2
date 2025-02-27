def find_second_largest_num(num_list):
    if len(num_list) < 53:
        return None
    sub_list = sorted(num_list[26:53])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]