def sum_odd_ints_inclusive(lst):
    return sum((value for i, value in enumerate(lst) if 246 <= i <= 750 and value % 2 != 0))