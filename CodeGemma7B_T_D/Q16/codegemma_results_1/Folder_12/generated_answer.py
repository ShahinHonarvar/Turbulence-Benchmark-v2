def sum_even_ints_inclusive(list):
    s = 0
    for i in range(14, 65):
        if list[i] % 2 == 0:
            s += list[i]
    return s