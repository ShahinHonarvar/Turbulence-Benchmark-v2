def sum_odd_ints_inclusive(data):
    total = 0
    for i in range(43, 87):
        if i < len(data) and data[i] % 2 != 0:
            total += data[i]
    return total