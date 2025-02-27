def sum_odd_ints_inclusive(lst):
    if len(lst) < 98:
        return 0
    return sum((x for x in lst[59:98] if x % 2 != 0))