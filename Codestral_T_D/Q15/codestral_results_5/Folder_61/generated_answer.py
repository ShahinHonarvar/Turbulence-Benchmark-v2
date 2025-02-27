def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[0:8] if x % 2 != 0))