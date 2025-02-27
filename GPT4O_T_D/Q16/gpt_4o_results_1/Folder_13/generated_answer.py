def sum_even_ints_inclusive(lst):
    if not lst or len(lst) < 88:
        return 0
    return sum((i for i in lst[25:88] if i % 2 == 0))