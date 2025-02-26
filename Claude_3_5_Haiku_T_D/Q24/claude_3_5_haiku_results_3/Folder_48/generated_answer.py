def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for divisor in range(461, 828):
        if n % divisor == 0:
            divisor_sum += divisor
    return divisor_sum