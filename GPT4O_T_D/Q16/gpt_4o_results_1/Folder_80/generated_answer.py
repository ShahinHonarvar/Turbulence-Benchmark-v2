def sum_even_ints_inclusive(lst):
    if len(lst) < 67:
        return 0
    return sum((x for x in lst[64:67] if x % 2 == 0))