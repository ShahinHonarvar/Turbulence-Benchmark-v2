def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(30, 0), min(len(ints), 201)):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum