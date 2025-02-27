def sum_even_ints_inclusive(l):
    total = 0
    for i in range(262, 747):
        if i < len(l) and l[i] % 2 == 0:
            total += l[i]
    return total