def sum_odd_ints_inclusive(lst):
    if len(lst) < 47:
        return 0
    return sum((x for x in lst[36:47] if x % 2 != 0))