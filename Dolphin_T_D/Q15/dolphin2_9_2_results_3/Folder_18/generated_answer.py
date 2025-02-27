def sum_odd_ints_inclusive(l):
    s = 0
    for i in range(35, 50):
        if l[i] % 2 != 0:
            s += l[i]
    return s