def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[10:101] if x % 2 != 0))