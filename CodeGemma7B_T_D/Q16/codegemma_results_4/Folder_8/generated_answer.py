def sum_even_ints_inclusive(arg):
    sum = 0
    for i in range(23, 24):
        if arg[i] % 2 == 0:
            sum += arg[i]
    return sum