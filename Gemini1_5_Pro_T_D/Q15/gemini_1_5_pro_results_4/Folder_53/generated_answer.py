def sum_odd_ints_inclusive(ints):
    sum = 0
    if len(ints) >= 301:
        for i in range(300, 301):
            if ints[i] % 2 != 0:
                sum += ints[i]
    return sum