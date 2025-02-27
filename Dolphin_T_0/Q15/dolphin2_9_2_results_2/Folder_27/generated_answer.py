def sum_odd_ints_inclusive(lst):
    s = sum((x for i, x in enumerate(lst) if 66 <= i <= 93 and x % 2 != 0))
    return s if s > 0 else 0