def sum_even_ints_inclusive(lst):
    if len(lst) > 41:
        return sum((i for i in lst[40:42] if i % 2 == 0))
    return 0