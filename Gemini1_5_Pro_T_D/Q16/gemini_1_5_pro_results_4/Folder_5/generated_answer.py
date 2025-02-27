def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(8, 10):
        if i >= len(ints):
            break
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum