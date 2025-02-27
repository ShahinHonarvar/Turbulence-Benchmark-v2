def sum_odd_ints_inclusive(lst):
    if len(lst) < 4:
        return 0
    return sum((x for x in lst[:4] if x % 2 != 0))