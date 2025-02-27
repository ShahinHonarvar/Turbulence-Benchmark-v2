def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[13:69:2] if i % 2 != 0))