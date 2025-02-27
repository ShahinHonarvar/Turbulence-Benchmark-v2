def find_second_smallest_num(num_list):
    if len(num_list) < 98:
        return None
    sub_list = num_list[20:98]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]