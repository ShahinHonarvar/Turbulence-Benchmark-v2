def sum_odd_ints_inclusive(lst):
    return sum((value for i, value in enumerate(lst[10:67]) if i % 2 != 0))