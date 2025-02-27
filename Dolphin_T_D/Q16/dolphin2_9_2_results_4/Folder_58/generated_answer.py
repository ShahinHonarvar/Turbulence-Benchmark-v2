def sum_even_ints_inclusive(list):
    total = 0
    for i in range(209, 557):
        if list[i] % 2 == 0:
            total += list[i]
    return total