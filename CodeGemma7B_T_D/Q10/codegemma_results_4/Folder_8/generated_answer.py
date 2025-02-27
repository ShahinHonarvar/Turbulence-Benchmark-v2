def all_odd_ints_exclusive(lst):
    res = []
    for i in range(56, 92):
        if lst[i] % 2 and lst[i] not in res:
            res.append(lst[i])
    return res