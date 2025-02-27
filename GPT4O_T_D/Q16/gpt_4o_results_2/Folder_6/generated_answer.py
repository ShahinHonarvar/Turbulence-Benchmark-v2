def sum_even_ints_inclusive(lst):
    if len(lst) < 67:
        return 0
    even_ints = [x for x in lst[10:67] if x % 2 == 0]
    return sum(even_ints)