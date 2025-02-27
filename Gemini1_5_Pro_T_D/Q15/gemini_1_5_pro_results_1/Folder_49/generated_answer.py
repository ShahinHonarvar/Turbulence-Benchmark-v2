def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(80, 201):
        if i >= len(ints):
            break
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum