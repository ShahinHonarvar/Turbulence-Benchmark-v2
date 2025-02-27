def sum_even_ints_inclusive(lst):
    if len(lst) < 21:
        return 0
    return sum((x for x in lst[20:31] if x % 2 == 0))