def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[60:201] if i % 2 != 0)) if len(lst) > 200 else 0