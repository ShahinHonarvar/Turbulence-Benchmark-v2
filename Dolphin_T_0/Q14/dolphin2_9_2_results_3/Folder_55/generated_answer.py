def find_second_smallest_num(num_list):
    if 10 < len(num_list) < 10:
        return None
    sub_list = num_list[10:11]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]