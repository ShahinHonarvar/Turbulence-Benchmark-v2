def sum_even_ints_inclusive(ints):
    sum_even_ints = 0
    for i in range(14, 65):
        if ints[i] % 2 == 0:
            sum_even_ints += ints[i]
    return sum_even_ints if sum_even_ints != 0 else 0