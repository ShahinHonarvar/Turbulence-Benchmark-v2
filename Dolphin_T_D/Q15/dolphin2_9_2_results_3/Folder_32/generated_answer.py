def sum_odd_ints_inclusive(l):
    s = 0
    for i in range(21, 98):
        if l[i] % 2 != 0:
            s += l[i]
    return s