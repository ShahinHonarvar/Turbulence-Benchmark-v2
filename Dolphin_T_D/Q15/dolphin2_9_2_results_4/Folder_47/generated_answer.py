def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[37:77:2] if x % 2 != 0))