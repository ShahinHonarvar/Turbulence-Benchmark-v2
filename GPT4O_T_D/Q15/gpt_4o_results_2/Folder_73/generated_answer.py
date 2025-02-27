def sum_odd_ints_inclusive(lst):
    if len(lst) < 20:
        return 0
    lst = lst[19:93]
    return sum((x for x in lst if x % 2 != 0))