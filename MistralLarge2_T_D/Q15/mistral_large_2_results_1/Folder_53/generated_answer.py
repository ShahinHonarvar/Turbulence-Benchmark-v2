def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[300:301] if x % 2 != 0))