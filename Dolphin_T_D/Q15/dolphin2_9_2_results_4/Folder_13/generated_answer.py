def sum_odd_ints_inclusive(lst):
    s = 0
    for i in range(25, 88):
        if lst[i] % 2 != 0:
            s += lst[i]
    if s == 0:
        return 0
    return s