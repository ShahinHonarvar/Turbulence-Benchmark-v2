def find_second_largest_num(lst):
    if 30 < len(lst):
        sub_lst = lst[19:31]
        if len(sub_lst) >= 2:
            sub_lst.sort()
            return sub_lst[-2]
    return None