def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[30:201] if x % 2 != 0))