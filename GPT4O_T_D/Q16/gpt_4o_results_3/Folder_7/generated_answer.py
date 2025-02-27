def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[661:925] if x % 2 == 0)) if 661 < len(lst) else 0