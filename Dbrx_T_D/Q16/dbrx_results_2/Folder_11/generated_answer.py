def sum_even_ints_inclusive(lst):
    if len(lst) < 52 or not all((isinstance(i, int) for i in lst)):
        return 'Invalid input'
    return sum((i for i in lst[37:52] if i % 2 == 0))