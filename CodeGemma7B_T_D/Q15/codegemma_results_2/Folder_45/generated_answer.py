def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(30, 201):
        if i % 2 != 0:
            sum += ints[i]
    return sum or 0