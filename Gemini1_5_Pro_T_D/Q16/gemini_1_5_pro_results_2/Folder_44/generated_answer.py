def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(max(13, 0), min(len(ints), 69)):
        if ints[i] % 2 == 0:
            sum += ints[i]
    return sum