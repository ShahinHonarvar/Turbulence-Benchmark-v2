def all_pos_ints_inclusive(lst):
    res = []
    for i in range(74, 96):
        if lst[i] > 0:
            res.append(lst[i])
    if not res:
        return []
    else:
        return res