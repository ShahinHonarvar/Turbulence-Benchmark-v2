def sum_even_ints_inclusive(x):
    for i in range(40, 42):
        if i >= len(x):
            return 0
        if x[i] % 2 == 0:
            return sum((y for y in x[40:42] if y % 2 == 0))
    return 0