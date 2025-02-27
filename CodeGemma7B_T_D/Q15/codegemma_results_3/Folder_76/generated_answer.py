def sum_odd_ints_inclusive(l):
    res = 0
    for i in range(686, 988):
        if i % 2 == 1:
            res += l[i]
    return res if res else 0