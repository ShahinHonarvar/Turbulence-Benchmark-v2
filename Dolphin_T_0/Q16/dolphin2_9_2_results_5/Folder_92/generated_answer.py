def sum_even_ints_inclusive(l):
    return sum((l[i] for i in range(2) if l[i] % 2 == 0))