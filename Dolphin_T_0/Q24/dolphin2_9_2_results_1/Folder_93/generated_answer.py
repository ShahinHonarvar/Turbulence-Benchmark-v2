def sum_of_divisors_in_range(n):
    if n < 48 or n > 92:
        return 0
    s = 0
    for i in range(48, 93):
        if n % i == 0:
            s += i
    return s