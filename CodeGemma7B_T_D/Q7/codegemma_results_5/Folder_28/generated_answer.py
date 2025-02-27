def all_even_ints_inclusive(lst):
    res = []
    for i in range(62, 64):
        if lst[i] % 2 == 0:
            res.append(lst[i])
    return res or []