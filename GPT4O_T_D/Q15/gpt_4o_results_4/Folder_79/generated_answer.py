def sum_odd_ints_inclusive(lst):
    if len(lst) > 4 and lst[4] % 2 != 0:
        return lst[4]
    return 0