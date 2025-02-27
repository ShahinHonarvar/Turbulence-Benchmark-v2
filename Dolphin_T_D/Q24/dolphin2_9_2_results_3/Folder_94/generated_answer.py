def sum_of_divisors_in_range(n):
    s = 0
    for i in range(35, 38):
        if n % i == 0:
            s += i
    if s == 0:
        return 0
    return s