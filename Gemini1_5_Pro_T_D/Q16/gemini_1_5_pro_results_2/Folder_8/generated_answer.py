def sum_even_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    if lst[23] % 2 == 0:
        return lst[23]
    else:
        return 0