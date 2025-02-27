def sum_odd_ints_inclusive(lst):
    return sum((val for val in lst[209:557] if val % 2 != 0))