def sum_odd_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    if lst[6] % 2 != 0:
        return lst[6]
    return 0