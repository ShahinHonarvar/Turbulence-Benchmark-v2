def sum_odd_ints_inclusive(lst):
    if len(lst) < 23:
        return 0
    else:
        return sum((x for x in lst[23:] if x % 2 != 0 and 23 <= lst.index(x) <= 23))