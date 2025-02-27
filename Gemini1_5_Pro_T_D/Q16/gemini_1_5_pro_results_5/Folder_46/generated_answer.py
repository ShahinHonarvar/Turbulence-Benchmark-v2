def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(30, 88):
        if i < len(ints) and ints[i] % 2 == 0:
            sum += ints[i]
    return sum