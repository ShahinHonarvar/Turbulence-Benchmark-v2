def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(22, 64):
        if i % 2 == 0:
            total += lst[i]
    return total if total != 0 else 0