def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst[14:65], 14) if val % 2 != 0))