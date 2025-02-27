def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst[29:80]) if val % 2 != 0))