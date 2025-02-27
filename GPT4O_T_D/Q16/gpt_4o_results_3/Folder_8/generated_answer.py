def sum_even_ints_inclusive(lst):
    if len(lst) <= 23:
        return 0
    return sum((i for i in lst[23:24] if i % 2 == 0))