def sum_even_ints_inclusive(l):
    return sum((i for i in l[0:5] if i % 2 == 0))