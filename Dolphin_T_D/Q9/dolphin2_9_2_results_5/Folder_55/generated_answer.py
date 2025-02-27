def all_odd_ints_inclusive(lst):
    res = []
    for i in range(10, 11):
        if lst[i] % 2 != 0:
            res.append(lst[i])
    return res