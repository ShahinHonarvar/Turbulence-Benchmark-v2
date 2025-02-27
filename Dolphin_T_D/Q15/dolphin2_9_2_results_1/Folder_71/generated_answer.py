def sum_odd_ints_inclusive(lst):
    return sum((value for index, value in enumerate(lst[26:53]) if index % 2 == 1))