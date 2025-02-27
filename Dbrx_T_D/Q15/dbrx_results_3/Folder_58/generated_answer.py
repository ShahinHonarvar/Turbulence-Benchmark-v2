def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[208:557] if x % 2 != 0))