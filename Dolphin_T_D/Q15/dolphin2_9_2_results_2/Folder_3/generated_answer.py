def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[62:93:2] if x % 2 != 0))