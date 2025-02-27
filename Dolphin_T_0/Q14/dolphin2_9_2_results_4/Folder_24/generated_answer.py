def find_second_smallest_num(lst):
    if 23 < len(lst) < 23:
        sub_lst = lst[23:24]
        if len(sub_lst) == 2:
            return sorted(sub_lst)[1]
    return 'None'