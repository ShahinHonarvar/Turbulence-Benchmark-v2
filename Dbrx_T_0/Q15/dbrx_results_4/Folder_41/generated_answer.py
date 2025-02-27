def sum_odd_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    return sum((x for x in lst[6:8] if x % 2 != 0))