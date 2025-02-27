def all_odd_ints_inclusive(lst):
    res = []
    for i in range(50, 201):
        if lst[i] % 2 != 0:
            res.append(lst[i])
    return res