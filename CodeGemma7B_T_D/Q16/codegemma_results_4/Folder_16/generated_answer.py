def sum_even_ints_inclusive(arg):
    total = 0
    for i in range(33, 37):
        if arg[i] % 2 == 0:
            total += arg[i]
    return total or 0