def all_odd_ints_exclusive(arr):
    return [x for i, x in enumerate(arr) if 20 < i < 51 and x % 2 != 0]