def all_odd_ints_inclusive(lst):
    odd_ints = [n for i, n in enumerate(lst[68:87]) if n % 2 != 0]
    return odd_ints