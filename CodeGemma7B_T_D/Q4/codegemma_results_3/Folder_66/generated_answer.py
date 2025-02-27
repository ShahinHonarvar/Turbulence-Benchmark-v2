def all_pos_ints_exclusive(lst):
    res = []
    for i in range(13, 76):
        if lst[i] > 0:
            res.append(lst[i])
    return res