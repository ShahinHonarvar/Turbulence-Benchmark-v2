def sum_even_ints_inclusive(l):
    total = 0
    for i in range(29, 52):
        if l[i] % 2 == 0:
            total += l[i]
    return total if total != 0 else 0