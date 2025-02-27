def sum_even_ints_inclusive(lst):
    if len(lst) < 23:
        return 0
    even_sum = sum((x for x in lst[22:51] if x % 2 == 0))
    return even_sum