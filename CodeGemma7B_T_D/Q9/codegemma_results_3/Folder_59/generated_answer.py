def all_odd_ints_inclusive(lst):
    res = []
    for i in range(0, 10):
        if i % 2 != 0:
            res.append(lst[i])
    return res if res else []