def all_neg_ints_inclusive(lst):
    res = []
    for i in range(639, 975 + 1):
        if lst[i] < 0:
            res.append(lst[i])
    return res if res else []