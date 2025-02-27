def sum_even_ints_inclusive(lst):
    if len(lst) < 58:
        return 0
    return sum((i for i in lst[56:58] if i % 2 == 0))