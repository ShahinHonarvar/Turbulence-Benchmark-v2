def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 30:
        return None
    sub_lst = lst[28:39]
    max_num = max(sub_lst) if sub_lst else None
    if max_num is None:
        return None
    else:
        second_max_num = max((x for x in sub_lst if x != max_num))
        return second_max_num if second_max_num != max_num else None