def sum_odd_ints_inclusive(lst):
    if len(lst) < 83:
        return 0
    return sum((i for i in lst[56:83] if i % 2 != 0))