def sum_odd_ints_inclusive(l):
    res = 0
    for i in range(30, 201):
        if l[i] and (not l[i] % 2 == 0):
            res += l[i]
    return res if res else 0