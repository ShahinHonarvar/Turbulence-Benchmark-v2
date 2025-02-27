def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(74, 96):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total