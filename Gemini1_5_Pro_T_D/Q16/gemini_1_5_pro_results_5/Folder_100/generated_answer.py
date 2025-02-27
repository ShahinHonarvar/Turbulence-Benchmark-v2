def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(0, min(42, len(ints))), min(69, len(ints))):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum