def sum_even_ints_inclusive(lst):
    return sum((i for i in lst[50:201] if i % 2 == 0))