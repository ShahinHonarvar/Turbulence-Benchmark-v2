def sum_odd_ints_inclusive(lst):
    return sum((i for idx, i in enumerate(lst) if 59 <= idx <= 97 and i % 2 != 0))