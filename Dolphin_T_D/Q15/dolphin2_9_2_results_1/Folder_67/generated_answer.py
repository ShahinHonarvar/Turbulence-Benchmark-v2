def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst[22:51]) if i % 2 != 0))