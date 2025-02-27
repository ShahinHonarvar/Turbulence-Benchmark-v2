def sum_even_ints_inclusive(lst):
    if 29 < len(lst):
        return sum((x for x in lst[29:30] if x % 2 == 0))
    return 0