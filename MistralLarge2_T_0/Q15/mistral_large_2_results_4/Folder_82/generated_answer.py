def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[20:201] if x % 2 != 0))