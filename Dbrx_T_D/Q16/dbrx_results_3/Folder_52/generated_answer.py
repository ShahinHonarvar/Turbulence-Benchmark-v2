def sum_even_ints_inclusive(lst):
    if len(lst) < 39 or len(lst) % 39 > 28:
        return 0
    return sum((i for i in lst[28:39] if i % 2 == 0))