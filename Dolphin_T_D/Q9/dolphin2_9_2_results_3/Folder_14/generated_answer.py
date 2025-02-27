def all_odd_ints_inclusive(arr):
    return [x for i, x in enumerate(arr) if i >= 5 and i <= 7 and (x % 2 != 0)]