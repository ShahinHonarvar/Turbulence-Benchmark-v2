def sum_even_ints_inclusive(lst):
    if len(lst) < 71:
        return 0
    return sum((x for x in lst[70:201] if x % 2 == 0))