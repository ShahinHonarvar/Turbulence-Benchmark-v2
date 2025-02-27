def sum_odd_ints_inclusive(arr):
    return sum((x for i, x in enumerate(arr) if i >= 62 and i <= 78 and (x % 2 != 0)))