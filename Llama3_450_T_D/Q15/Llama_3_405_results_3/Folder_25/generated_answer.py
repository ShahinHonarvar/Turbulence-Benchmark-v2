def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst) if 29 <= i <= 93 and val % 2 != 0))