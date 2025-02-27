def sum_even_ints_inclusive(ls):
    total = 0
    for i in range(56, 58):
        if ls[i] % 2 == 0:
            total += ls[i]
    return total if total else 0