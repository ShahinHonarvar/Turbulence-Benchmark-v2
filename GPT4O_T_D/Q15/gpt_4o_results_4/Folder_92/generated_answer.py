def sum_odd_ints_inclusive(lst):
    if len(lst) < 2:
        return 0
    return sum((x for x in lst[1:2] if x % 2 != 0))