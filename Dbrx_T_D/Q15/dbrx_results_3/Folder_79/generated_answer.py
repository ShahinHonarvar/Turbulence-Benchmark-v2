def sum_odd_ints_inclusive(lst):
    if len(lst) <= 4:
        return 0
    elif len(lst) < 8:
        return sum((x for x in lst[4:] if x % 2 != 0))
    else:
        return sum((x for x in lst[4:8] if x % 2 != 0))