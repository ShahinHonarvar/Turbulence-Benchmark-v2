def sum_even_ints_inclusive(ints):
    even_sum = 0
    for i in range(13, 70, 2):
        if i < len(ints):
            even_sum += ints[i]
    return even_sum