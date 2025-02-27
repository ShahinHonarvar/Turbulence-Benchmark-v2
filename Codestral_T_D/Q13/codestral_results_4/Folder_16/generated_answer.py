def find_second_largest_num(lst):
    sub_lst = lst[33:37]
    sub_lst.sort()
    if len(sub_lst) < 2:
        return None
    else:
        return sub_lst[-2]