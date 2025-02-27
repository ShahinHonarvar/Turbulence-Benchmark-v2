def all_even_ints_exclusive(lst):
    res = []
    for i in range(15, 99):
        if lst[i] % 2 == 0:
            res.append(lst[i])
    return res