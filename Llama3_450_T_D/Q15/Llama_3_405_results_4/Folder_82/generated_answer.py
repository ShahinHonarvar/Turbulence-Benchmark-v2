def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst) if 20 <= idx <= 200 and val % 2 != 0))