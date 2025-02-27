def sum_odd_ints_inclusive(lst):
    if not lst or len(lst) < 88:
        return 0
    return sum((x for x in lst[24:88] if x % 2 != 0))