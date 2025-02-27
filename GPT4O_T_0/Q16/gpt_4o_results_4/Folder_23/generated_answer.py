def sum_even_ints_inclusive(lst):
    if len(lst) < 72:
        return 0
    return sum((x for x in lst[52:72] if x % 2 == 0))