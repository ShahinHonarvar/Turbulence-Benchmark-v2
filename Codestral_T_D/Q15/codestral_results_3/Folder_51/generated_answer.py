def sum_odd_ints_inclusive(lst):
    return sum((n for n in lst[1:9] if n % 2 != 0))