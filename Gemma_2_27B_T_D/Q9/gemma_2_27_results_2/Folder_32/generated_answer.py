def all_odd_ints_inclusive(arr):
    return [x for i, x in enumerate(arr) if i >= 21 and i <= 97 and (x % 2 != 0)]