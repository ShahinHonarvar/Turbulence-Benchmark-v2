def sum_odd_ints_inclusive(lst):
    return sum((val for index, val in enumerate(lst[262:747]) if val % 2 != 0))