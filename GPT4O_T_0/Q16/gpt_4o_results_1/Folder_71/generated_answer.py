def sum_even_ints_inclusive(lst):
    if len(lst) < 53:
        return 0
    return sum((x for x in lst[26:53] if x % 2 == 0))