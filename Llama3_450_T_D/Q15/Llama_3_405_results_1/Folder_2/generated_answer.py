def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst) if 15 <= idx <= 39 and val % 2 != 0))