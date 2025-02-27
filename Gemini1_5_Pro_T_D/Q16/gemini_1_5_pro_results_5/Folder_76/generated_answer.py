def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(686, 0), min(len(ints), 988)):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum