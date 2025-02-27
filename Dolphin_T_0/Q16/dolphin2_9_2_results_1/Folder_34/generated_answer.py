def sum_even_ints_inclusive(lst):
    return sum((n for n in lst[60:201] if n % 2 == 0))