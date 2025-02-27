def find_second_largest_num(lst):
    sub_lst = lst[533:606]
    if len(sub_lst) < 2:
        return None
    else:
        return sorted(sub_lst)[-2]