def sum_even_ints_inclusive(ints):
    even_sum = 0
    for i in range(28, 41):
        if ints[i] % 2 == 0:
            even_sum += ints[i]
    return even_sum if even_sum != 0 else 0