def sum_even_ints_inclusive(data):
    sum = 0
    for i in range(82, 87):
        if i < len(data) and data[i] % 2 == 0:
            sum += data[i]
    return sum