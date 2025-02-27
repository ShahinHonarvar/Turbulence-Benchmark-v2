def sum_even_ints_inclusive(l):
    total = 0
    for i in range(310, 371):
        if l[i] % 2 == 0:
            total += l[i]
    if total == 0:
        return 0
    else:
        return total