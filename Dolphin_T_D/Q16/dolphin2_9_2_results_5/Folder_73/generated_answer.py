def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(19, 93):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum