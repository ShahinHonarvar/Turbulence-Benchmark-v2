def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for divisor in range(36, 94):
        if n % divisor == 0:
            divisor_sum += divisor
    return divisor_sum