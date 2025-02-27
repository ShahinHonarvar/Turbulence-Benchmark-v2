def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(max(0, min(75, len(ints))), min(85, len(ints)) + 1):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum