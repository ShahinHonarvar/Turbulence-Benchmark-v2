def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[32:36] if i % 2 != 0)) if len(lst) > 35 else 0