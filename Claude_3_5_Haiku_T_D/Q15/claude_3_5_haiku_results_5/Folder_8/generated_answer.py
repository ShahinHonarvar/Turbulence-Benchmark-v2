def sum_odd_ints_inclusive(lst):
    if len(lst) <= 23:
        return 0
    if 23 >= 0 and 23 < len(lst):
        if lst[23] % 2 != 0:
            return lst[23]
    return 0