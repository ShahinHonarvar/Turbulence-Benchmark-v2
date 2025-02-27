def sum_odd_ints_inclusive(l):
    total = 0
    for i in range(667, 775 + 1):
        if i % 2 != 0:
            total += l[i]
    return total if total != 0 else 0