def sum_odd_ints_inclusive(lst):
    if len(lst) < 2:
        return 0
    else:
        return sum((i for i in lst[1:1 + 1] if i % 2 != 0))