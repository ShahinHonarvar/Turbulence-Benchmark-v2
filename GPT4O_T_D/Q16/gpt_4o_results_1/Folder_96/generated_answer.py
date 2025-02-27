def sum_even_ints_inclusive(lst):
    if not lst or len(lst) <= 50:
        return 0
    return sum((i for i in lst[50:201] if i % 2 == 0))