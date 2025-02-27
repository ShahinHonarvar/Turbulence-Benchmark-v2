def sum_even_ints_inclusive(lst):
    if len(lst) < 52:
        return 0
    return sum((x for x in lst[37:52] if x % 2 == 0))