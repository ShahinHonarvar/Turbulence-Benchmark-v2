def sum_odd_ints_inclusive(ints):
    return sum((x for x in ints[:5] if x % 2 != 0))