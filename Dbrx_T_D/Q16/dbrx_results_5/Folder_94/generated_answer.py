def sum_even_ints_inclusive(lst):
    if not lst or len(lst) < 41:
        return 0
    return sum((i for i in lst[28:41] if i % 2 == 0))