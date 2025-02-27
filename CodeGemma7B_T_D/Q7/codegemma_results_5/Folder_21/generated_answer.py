def all_even_ints_inclusive(lst):
    res = []
    if not lst:
        return []
    for i in range(639, 976):
        if lst[i] % 2 == 0:
            res.append(lst[i])
    return res