def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for divisor in range(2, 4):
        if n % divisor == 0:
            divisors_sum += divisor
    return divisors_sum