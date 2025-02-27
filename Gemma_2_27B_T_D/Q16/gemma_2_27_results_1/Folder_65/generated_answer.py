def sum_even_ints_inclusive(data):
    sum = 0
    for i in range(56, 99):
        if data[i] % 2 == 0:
            sum += data[i]
    return sum