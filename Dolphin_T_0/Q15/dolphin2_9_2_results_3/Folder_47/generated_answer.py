def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst[37:77]) if val % 2 != 0))