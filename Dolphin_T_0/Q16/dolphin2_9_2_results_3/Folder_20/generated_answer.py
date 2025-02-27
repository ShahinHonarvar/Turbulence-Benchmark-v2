def sum_even_ints_inclusive(l):
    total = 0
    for i in range(56, 67):
        if i < len(l) and type(l[i]) == int and (l[i] % 2 == 0):
            total += l[i]
    return total if total != 0 else 0