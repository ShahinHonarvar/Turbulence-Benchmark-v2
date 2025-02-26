def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for divisor in range(11, 42):
        if n % divisor == 0:
            divisors_sum += divisor
    return divisors_sum