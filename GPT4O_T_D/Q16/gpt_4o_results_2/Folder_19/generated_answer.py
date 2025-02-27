def sum_even_ints_inclusive(lst):
    if len(lst) < 6:
        return 0
    return sum((n for n in lst[3:6] if n % 2 == 0))