def sum_even_ints_inclusive(l):
    total = 0
    for i in range(56, 99):
        if l[i] % 2 == 0:
            total += l[i]
    return total