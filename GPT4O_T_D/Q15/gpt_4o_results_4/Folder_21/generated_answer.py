def sum_odd_ints_inclusive(lst):
    if 639 > len(lst) - 1 or 975 > len(lst) - 1:
        return 0
    return sum((x for x in lst[639:976] if x % 2 != 0))