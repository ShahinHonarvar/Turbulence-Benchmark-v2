def sum_odd_ints_inclusive(lst):
    odd_ints = lst[13:69]
    return sum((x for x in odd_ints if x % 2 != 0))