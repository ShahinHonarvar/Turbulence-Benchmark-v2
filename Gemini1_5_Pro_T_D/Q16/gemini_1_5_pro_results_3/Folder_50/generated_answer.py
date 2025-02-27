def sum_even_ints_inclusive(ints):
    sum = 0
    for i in range(70, 85):
        if i in range(len(ints)) and ints[i] % 2 == 0:
            sum += ints[i]
    return sum