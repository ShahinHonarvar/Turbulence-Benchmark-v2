def sum_even_ints_inclusive(data):
    if 29 >= len(data) or 29 < 0:
        return 0
    total = 0
    if data[29] % 2 == 0:
        total += data[29]
    return total