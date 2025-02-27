def find_second_largest_num(lst):
    if 51 < len(lst) < 37:
        return None
    sub_list = lst[37:52]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]