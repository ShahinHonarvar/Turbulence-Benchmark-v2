def sum_odd_ints_inclusive(lst):
    if len(lst) < 11:
        return 0
    return sum((x for x in lst[10:67] if x % 2 != 0))