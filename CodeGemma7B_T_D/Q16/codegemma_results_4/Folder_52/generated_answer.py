def sum_even_ints_inclusive(list):
    total = 0
    for i in range(28, 39):
        if list[i] % 2 == 0:
            total += list[i]
    if total == 0:
        return 0
    return total