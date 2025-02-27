def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst) if 27 <= idx <= 55 and val % 2 != 0))