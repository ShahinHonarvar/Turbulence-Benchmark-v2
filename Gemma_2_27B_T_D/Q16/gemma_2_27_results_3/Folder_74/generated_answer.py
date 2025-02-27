def sum_even_ints_inclusive(data):
    sum = 0
    for i in range(17, 79):
        if data[i] % 2 == 0:
            sum += data[i]
    return sum