def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(31, 73):
        if int(ints[i]) % 2 != 0:
            sum += int(ints[i])
    return sum