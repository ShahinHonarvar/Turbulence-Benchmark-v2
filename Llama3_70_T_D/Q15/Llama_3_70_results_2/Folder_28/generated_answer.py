def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[62:64] if i % 2 != 0)) if len(lst) > 63 else 0