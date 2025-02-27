def sum_even_ints_inclusive(lst):
    if 6 < len(lst):
        return sum((x for x in lst[6:7] if x % 2 == 0))
    return 0