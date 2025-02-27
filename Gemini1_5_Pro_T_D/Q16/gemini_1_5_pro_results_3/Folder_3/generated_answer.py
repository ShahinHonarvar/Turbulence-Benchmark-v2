def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(0, min(62, len(ints))), min(93, len(ints))):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum