def sum_even_ints_inclusive(a):
    sum_even = 0
    for i in range(62, 64):
        if a[i] % 2 == 0:
            sum_even += a[i]
    return sum_even