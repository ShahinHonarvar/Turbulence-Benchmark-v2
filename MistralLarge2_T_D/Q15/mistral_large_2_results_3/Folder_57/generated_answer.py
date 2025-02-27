def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[27:56] if x % 2 != 0)) if lst else 0