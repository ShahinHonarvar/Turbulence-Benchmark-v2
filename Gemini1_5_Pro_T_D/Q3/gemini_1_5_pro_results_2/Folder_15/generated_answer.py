def all_pos_ints_inclusive(lst):
    res = []
    for i in range(4):
        if i < len(lst) and lst[i] > 0:
            res.append(lst[i])
    return res