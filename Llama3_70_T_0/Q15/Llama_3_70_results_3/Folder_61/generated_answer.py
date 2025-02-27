def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[:8] if i % 2 != 0))