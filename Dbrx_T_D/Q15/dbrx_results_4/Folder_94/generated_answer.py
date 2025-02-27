def sum_odd_ints_inclusive(lst):
    sublst = lst[27:41]
    result = sum((x for x in sublst if x % 2 != 0))
    return result