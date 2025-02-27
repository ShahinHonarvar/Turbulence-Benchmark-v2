def all_pos_ints_inclusive(lst):
    res = []
    for i in range(1, 6):
        if i in lst:
            res.append(i)
    return res