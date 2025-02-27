def sum_even_ints_inclusive(lst):
    if len(lst) < 65:
        lst = lst + [0] * (65 - len(lst))
    return sum((x for x in lst[14:65] if x % 2 == 0))