def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[62:79]) if i % 2 != 0))