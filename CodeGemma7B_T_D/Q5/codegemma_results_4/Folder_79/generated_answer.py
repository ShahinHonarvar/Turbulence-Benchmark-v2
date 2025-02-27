def all_neg_ints_inclusive(lst):
    if min(lst) >= 0 or max(lst) < 0 or len(lst) < 4:
        return []
    res = []
    for i in range(4, len(lst)):
        if lst[i] <= 0:
            res.append(lst[i])
    return res