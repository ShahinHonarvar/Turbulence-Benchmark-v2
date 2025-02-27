def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(22, 0), min(len(ints), 89)):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum