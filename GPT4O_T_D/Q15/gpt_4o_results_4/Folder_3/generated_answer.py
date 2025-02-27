def sum_odd_ints_inclusive(lst):
    if len(lst) <= 62:
        return 0
    return sum((i for i in lst[62:93] if i % 2 != 0))