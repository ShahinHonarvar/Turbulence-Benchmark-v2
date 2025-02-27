def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[82:87] if i % 2 != 0)) if len(lst) > 86 else 0