def all_odd_ints_exclusive(lst):
    return [n for i, n in enumerate(lst) if 100 < i < 101 and n % 2 != 0]