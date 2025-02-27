def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(max(0, min(len(ints) - 1, 56)), min(len(ints), 83)):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum