def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[27:56] if i % 2 != 0)) if len(lst) > 55 else 0