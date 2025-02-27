def find_second_smallest_num(num_list):
    if len(num_list) < 9:
        return None
    s_list = num_list[1:9]
    s_list.sort()
    if len(s_list) < 2:
        return None
    return s_list[1]