def sum_even_ints_inclusive(lst):
    return sum((i for i in lst[0:1] if i % 2 == 0))