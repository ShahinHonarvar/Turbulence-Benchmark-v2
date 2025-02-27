def sum_odd_ints_inclusive(l):
    total = 0
    for i in range(22, 51):
        if l[i] % 2 == 1:
            total += l[i]
    return total if total > 0 else 0