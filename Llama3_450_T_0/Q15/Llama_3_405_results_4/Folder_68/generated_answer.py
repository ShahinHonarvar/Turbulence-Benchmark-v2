def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[:9] if i % 2 != 0))