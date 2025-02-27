def sum_even_ints_inclusive(lst):
    s = 0
    for i in range(0, 1):
        if lst[i] % 2 == 0:
            s += lst[i]
    if s == 0:
        return 0
    else:
        return s