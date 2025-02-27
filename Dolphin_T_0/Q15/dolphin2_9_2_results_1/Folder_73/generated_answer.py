def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst[19:93]) if idx % 2 != 0))