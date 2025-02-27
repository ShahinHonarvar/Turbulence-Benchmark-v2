def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[300:301] if isinstance(x, int) and x % 2 != 0)) or 0