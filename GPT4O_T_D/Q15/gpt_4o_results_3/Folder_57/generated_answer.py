def sum_odd_ints_inclusive(lst):
    if len(lst) < 28:
        return 0
    return sum((i for i in lst[27:56] if i % 2 != 0))