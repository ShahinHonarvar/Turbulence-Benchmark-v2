def sum_odd_ints_inclusive(lst):
    if len(lst) < 95 or len(lst) < 74:
        return 0
    else:
        return sum((x for x in lst[74:96] if x % 2 != 0))