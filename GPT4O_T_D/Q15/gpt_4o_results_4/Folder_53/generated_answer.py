def sum_odd_ints_inclusive(lst):
    if len(lst) <= 300:
        return 0
    return sum((i for i in lst[300:301] if i % 2 != 0))