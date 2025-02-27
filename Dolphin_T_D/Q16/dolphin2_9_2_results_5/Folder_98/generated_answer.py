def sum_even_ints_inclusive(l):
    return sum((x for x in l[:7] if x % 2 == 0))