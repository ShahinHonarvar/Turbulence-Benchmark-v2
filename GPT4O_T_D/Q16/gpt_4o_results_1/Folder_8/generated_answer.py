def sum_even_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    total = 0
    for i in range(23, 24):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total