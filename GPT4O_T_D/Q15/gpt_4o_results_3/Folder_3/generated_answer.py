def sum_odd_ints_inclusive(lst):
    if 62 > len(lst) - 1 or 92 > len(lst) - 1:
        return 0
    return sum((x for x in lst[62:93] if x % 2 != 0))