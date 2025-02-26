def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0 and 38 <= divisor <= 65:
            divisor_sum += divisor
    return divisor_sum