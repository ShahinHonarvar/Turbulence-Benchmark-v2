def sum_odd_ints_inclusive(lst):
    if len(lst) < 2:
        return 0
    return sum((i for i in lst[1:] if i % 2 != 0))