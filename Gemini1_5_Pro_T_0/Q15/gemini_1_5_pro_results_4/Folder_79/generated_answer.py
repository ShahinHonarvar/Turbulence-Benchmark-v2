def sum_odd_ints_inclusive(lst):
    if len(lst) < 5:
        return 0
    if lst[4] % 2 == 0:
        return 0
    else:
        return lst[4]