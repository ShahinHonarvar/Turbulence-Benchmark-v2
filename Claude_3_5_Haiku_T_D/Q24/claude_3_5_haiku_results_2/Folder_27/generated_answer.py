def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for d in range(15, 21):
        if n % d == 0:
            divisor_sum += d
    return divisor_sum