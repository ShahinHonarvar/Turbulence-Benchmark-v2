def sum_even_ints_inclusive(x):
    sum = 0
    for i in range(70, 85):
        if x[i] % 2 == 0:
            sum += x[i]
    if sum == 0:
        return 0
    else:
        return sum