def sum_even_ints_inclusive(lst):
    if len(lst) < 33:
        return 0
    return sum((x for x in lst[28:33] if x % 2 == 0))