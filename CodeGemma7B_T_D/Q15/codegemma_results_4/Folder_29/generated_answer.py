def sum_odd_ints_inclusive(lst):
    lst = lst[59:98]
    return sum((n for n in lst if n % 2 != 0))