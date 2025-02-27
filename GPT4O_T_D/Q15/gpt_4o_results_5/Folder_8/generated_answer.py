def sum_odd_ints_inclusive(lst):
    if len(lst) <= 23:
        return 0
    if lst[23] % 2 != 0:
        return lst[23]
    return 0