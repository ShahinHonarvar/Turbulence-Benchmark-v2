def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0 and 586 <= divisor <= 840:
            divisors_sum += divisor
    return divisors_sum