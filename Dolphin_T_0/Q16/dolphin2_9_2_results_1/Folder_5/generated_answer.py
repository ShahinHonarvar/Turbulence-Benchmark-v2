def sum_even_ints_inclusive(ints):
    even_sum = 0
    for i in range(8, 10):
        if ints[i] % 2 == 0:
            even_sum += ints[i]
    return even_sum