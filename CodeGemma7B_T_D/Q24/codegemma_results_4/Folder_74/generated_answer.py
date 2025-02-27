def sum_of_divisors_in_range(n):
    s = 0
    for i in range(40, 75):
        if n % i == 0:
            s += i
    if s == 0:
        return 0
    else:
        return s