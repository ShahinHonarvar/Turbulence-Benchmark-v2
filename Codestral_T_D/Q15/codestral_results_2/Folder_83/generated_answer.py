def sum_odd_ints_inclusive(lst):
    return sum((v for v in lst[90:201] if v % 2 != 0))