def sum_even_ints_inclusive(lst):
    if len(lst) < 37:
        return 0
    return sum((x for x in lst[33:37] if x % 2 == 0))