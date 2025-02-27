def all_pos_ints_inclusive(lst):
    res = []
    for i in range(29, 52):
        if lst[i] > 0:
            res.append(lst[i])
    return res or []