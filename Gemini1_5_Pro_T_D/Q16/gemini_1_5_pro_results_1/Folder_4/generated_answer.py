def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(12, 0), min(len(ints), 93)):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum