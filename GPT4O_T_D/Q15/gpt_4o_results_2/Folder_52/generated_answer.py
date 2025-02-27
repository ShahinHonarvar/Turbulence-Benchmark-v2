def sum_odd_ints_inclusive(lst):
    if len(lst) <= 38:
        return 0
    return sum((x for x in lst[28:39] if x % 2 != 0))