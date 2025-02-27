def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[246:751:2] if x % 2 != 0))