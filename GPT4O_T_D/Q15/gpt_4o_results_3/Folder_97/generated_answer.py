def sum_odd_ints_inclusive(lst):
    if len(lst) < 41:
        return 0
    return sum((x for x in lst[40:81] if x % 2 != 0))