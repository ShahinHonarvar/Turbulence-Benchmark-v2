def sum_even_ints_inclusive(lst):
    if len(lst) < 11:
        return 0
    if len(lst) > 101:
        lst = lst[:101]
    return sum((x for x in lst[10:101] if x % 2 == 0))