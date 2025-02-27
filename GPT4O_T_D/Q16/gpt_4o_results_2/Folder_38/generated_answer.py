def sum_even_ints_inclusive(lst):
    if len(lst) < 23:
        return 0
    return sum((i for i in lst[22:64] if i % 2 == 0))