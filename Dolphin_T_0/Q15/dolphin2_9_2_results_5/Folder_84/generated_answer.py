def sum_odd_ints_inclusive(lst):
    return sum((value for i, value in enumerate(lst) if i in range(43, 87) and value % 2 == 1))