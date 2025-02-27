def all_odd_ints_inclusive(a):
    return [x for i, x in enumerate(a) if x % 2 != 0 and 30 <= i <= 48]