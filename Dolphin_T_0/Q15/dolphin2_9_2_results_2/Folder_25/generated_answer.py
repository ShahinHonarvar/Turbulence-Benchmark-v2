def sum_odd_ints_inclusive(lst):
    return sum((val for val in lst[29:94:2] if val % 2 != 0))