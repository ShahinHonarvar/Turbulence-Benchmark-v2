def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst[533:606]) if val % 2 != 0))