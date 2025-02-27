def sum_even_ints_inclusive(x):
    sum = 0
    for i in range(50, 201):
        if x[i] % 2 == 0:
            sum += x[i]
    return sum