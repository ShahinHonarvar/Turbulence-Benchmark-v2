def find_second_smallest_num(lst):
    if len(lst) <= 92:
        return None
    sub_list = lst[19:93]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]