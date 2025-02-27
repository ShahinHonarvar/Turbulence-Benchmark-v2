def sum_odd_ints_inclusive(data):
    total = 0
    for i in range(26, 53):
        if i < len(data) and data[i] % 2 != 0:
            total += data[i]
    return total