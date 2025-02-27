def sum_odd_ints_inclusive(ints):
    sum = 0
    if len(ints) >= 64:
        for i in range(62, 64):
            if ints[i] % 2 != 0:
                sum += ints[i]
    return sum