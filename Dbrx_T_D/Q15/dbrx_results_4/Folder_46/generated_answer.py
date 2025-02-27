def sum_odd_ints_inclusive(lst):
    if not lst or len(lst) < 88:
        return 0
    return sum((i for i in lst[30:88] if i % 2 != 0))