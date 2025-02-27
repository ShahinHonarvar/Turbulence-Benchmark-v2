def sum_even_ints_inclusive(lst):
    s = 0
    for i in range(262, 747):
        if lst[i] % 2 == 0:
            s += lst[i]
    return s if s != 0 else None