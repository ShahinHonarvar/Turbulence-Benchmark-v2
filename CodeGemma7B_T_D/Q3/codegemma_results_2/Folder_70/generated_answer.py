def all_pos_ints_inclusive(lst):
    lst = lst[28:33]
    res = []
    for x in lst:
        if x > 0:
            res += [x]
    return res or []