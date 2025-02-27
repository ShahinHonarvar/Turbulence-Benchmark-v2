def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(21, 98):
        if i in range(len(ints)):
            if ints[i] % 2 != 0:
                sum += ints[i]
    return sum