def find_second_largest_num(lst):
    sub_lst = lst[533:606]
    sub_lst.sort()
    if len(sub_lst) >= 2:
        return sub_lst[-2]
    else:
        return None