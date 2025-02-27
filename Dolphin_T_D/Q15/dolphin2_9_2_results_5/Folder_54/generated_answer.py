def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[34:56:2] if x % 2 != 0))