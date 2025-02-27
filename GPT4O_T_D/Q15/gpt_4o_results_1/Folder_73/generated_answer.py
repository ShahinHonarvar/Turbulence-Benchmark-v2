def sum_odd_ints_inclusive(lst):
    if len(lst) < 20:
        return 0
    return sum((i for i in lst[19:93] if i % 2 != 0))