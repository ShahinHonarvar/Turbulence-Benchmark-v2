def sum_odd_ints_inclusive(lst):
    if 209 < len(lst) and 556 < len(lst):
        return sum((x for x in lst[209:557:2] if x % 2 != 0))
    else:
        return 0