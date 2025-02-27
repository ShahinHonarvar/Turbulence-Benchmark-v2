def sum_odd_ints_inclusive(lst):
    if len(lst) == 0:
        return 0
    if lst[0] % 2 != 0:
        return lst[0]
    else:
        return 0