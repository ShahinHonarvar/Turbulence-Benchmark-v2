def all_odd_ints_inclusive(lst):
    odd_ints = [x for i, x in enumerate(lst) if 68 <= i <= 86 and x % 2 != 0]
    return odd_ints