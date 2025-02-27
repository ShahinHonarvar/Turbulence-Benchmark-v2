def sum_odd_ints_inclusive(lst):
    if len(lst) >= 2:
        return sum((x for x in lst[1:1 + 1] if x % 2 != 0))
    else:
        return 0