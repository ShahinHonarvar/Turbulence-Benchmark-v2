def all_neg_ints_inclusive(l):
    res = []
    for i in range(246, 751):
        if l[i] < 0:
            res.append(l[i])
    return res