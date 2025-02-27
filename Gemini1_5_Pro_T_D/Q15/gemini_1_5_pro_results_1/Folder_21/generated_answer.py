def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(max(639, 0), min(976, len(ints))):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum