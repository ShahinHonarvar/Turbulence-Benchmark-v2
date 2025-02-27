def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[3:6] if x % 2 != 0))