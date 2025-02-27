def sum_odd_ints_inclusive(lst):
    if len(lst) < 371:
        return 0
    return sum((x for x in lst[310:371] if x % 2 != 0))