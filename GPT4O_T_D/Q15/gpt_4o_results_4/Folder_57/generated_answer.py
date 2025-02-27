def sum_odd_ints_inclusive(lst):
    if len(lst) < 28:
        return 0
    return sum((x for x in lst[27:56] if x % 2 != 0))