def sum_odd_ints_inclusive(lst):
    if len(lst) < 83:
        return 0
    return sum((x for x in lst[56:83] if x % 2 != 0))