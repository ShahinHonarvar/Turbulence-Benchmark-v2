def sum_odd_ints_inclusive(lst):
    subset = lst[74:96]
    return sum((x for x in subset if x % 2 != 0))