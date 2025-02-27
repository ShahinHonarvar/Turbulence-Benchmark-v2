def sum_even_ints_inclusive(lst):
    t = sum((x for x in lst[62:79:1] if x % 2 == 0))
    return t if t != 0 else 0