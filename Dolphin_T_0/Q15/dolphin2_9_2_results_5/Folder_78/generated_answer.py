def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst) if i >= 43 and i <= 51 and (val % 2 != 0)))