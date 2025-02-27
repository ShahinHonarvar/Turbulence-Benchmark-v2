def sum_of_divisors_in_range(a):
    i, c = (39, 0)
    while i <= 43:
        if a % i == 0:
            c += i
        i += 1
    if c is not 0:
        return c
    else:
        return 0