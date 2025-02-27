def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(max(29, 0), min(len(ints), 94)):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum