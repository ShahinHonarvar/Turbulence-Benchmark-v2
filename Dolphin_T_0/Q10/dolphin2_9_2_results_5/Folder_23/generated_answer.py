def all_odd_ints_exclusive(lst):
    res = []
    for i in range(29, 53):
        if lst[i] % 2 != 0:
            res.append(lst[i])
    return res