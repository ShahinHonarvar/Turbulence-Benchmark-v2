def sum_odd_ints_inclusive(lst):
    if len(lst) < 85:
        return 0
    return sum((x for x in lst[70:85] if x % 2 != 0))