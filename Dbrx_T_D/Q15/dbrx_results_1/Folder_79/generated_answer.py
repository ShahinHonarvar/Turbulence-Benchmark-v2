def sum_odd_ints_inclusive(lst):
    if len(lst) <= 4:
        return 0
    else:
        return sum((x for x in lst[4:5] if x % 2 != 0))