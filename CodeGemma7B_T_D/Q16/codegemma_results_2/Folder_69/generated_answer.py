def sum_even_ints_inclusive(l):
    sum = 0
    for i in range(32, 36):
        if l[i] % 2 == 0:
            sum += l[i]
    if sum == 0:
        return 0
    else:
        return sum