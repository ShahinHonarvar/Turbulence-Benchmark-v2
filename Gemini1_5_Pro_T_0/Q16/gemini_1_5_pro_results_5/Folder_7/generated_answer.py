def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(661, len(ints))):
        if i >= 661 and i <= 924 and (ints[i] % 2 == 0):
            sum += ints[i]
    return sum