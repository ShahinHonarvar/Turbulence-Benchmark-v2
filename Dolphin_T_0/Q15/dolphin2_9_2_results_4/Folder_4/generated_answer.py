def sum_odd_ints_inclusive(lst):
    return sum((value for value in lst[12:93] if value % 2 != 0))