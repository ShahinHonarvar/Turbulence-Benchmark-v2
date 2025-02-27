def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[262:747]) if i % 2 == 1))