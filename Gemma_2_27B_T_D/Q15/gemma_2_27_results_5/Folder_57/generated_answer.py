def sum_odd_ints_inclusive(data):
    total = 0
    for i in range(27, 56):
        if data[i] % 2 != 0:
            total += data[i]
    return total