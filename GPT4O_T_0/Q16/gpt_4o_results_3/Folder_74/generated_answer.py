def sum_even_ints_inclusive(lst):
    if len(lst) < 79:
        return 0
    return sum((x for x in lst[17:79] if x % 2 == 0))