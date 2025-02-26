def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for d in range(60, 87):
        if n % d == 0:
            divisors_sum += d
    return divisors_sum