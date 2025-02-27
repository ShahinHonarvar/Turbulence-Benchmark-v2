def sum_even_ints_inclusive(lst):
    res = 0
    for i in range(6, 7):
        if lst[i] % 2 == 0:
            res += lst[i]
    return res