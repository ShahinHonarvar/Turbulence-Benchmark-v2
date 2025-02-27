def sum_odd_ints_inclusive(lst):
    if len(lst) < 5:
        return 0
    return sum((x for x in lst[4:5] if x % 2 != 0))