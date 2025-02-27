def sum_even_ints_inclusive(l_of_ints):
    total = 0
    for i in range(639, 976):
        if l_of_ints[i] % 2 == 0:
            total += l_of_ints[i]
    return total