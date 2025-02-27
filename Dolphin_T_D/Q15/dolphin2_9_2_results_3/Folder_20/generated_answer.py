def sum_odd_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst[56:67]) if val % 2 == 1))