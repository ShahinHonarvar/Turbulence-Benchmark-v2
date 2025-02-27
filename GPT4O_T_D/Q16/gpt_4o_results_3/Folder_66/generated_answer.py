def sum_even_ints_inclusive(lst):
    if len(lst) < 55:
        return 0
    return sum((x for x in lst[50:55] if x % 2 == 0))