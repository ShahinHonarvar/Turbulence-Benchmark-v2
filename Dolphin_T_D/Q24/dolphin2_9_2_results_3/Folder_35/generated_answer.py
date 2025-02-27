def sum_of_divisors_in_range(n):
    sum = 0
    for d in range(392, 466):
        if n % d == 0:
            sum += d
    return sum