def find_second_largest_num(lst):
    if not lst:
        return None
    s_lst = lst[75:89]
    if len(s_lst) == 1 or len(s_lst) == 0:
        return None
    l1, l2 = sorted(s_lst)[-2:]
    if l1 == l2:
        return l2 if l1 in lst else None
    return l1