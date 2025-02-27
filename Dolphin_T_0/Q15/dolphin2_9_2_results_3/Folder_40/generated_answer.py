def sum_odd_ints_inclusive(arr):
    return sum((val for index, val in enumerate(arr[:3]) if val % 2 != 0))