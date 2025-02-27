def sum_odd_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    return sum((x for x in lst[23:24] if x % 2 != 0))