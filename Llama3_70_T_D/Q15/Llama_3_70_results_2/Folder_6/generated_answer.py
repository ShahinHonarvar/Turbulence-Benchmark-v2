def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[10:67]) if x % 2 != 0))