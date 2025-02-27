def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(42, 69):
        if i in range(0, len(ints)):
            if ints[i] % 2 != 0:
                sum += ints[i]
    return sum