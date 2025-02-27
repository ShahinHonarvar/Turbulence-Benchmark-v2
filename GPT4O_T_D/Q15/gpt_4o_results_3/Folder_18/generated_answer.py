def sum_odd_ints_inclusive(lst):
    if len(lst) < 50:
        return 0
    return sum((x for x in lst[35:50] if x % 2 != 0))