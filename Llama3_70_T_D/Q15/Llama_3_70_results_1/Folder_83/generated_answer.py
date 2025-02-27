def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[90:201], 90) if x % 2 != 0))