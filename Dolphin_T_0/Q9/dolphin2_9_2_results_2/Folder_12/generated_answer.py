def all_odd_ints_inclusive(lst):
    result = [x for i, x in enumerate(lst) if 14 <= i <= 64 and x % 2 != 0]
    return result