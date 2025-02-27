def sum_of_divisors_in_range(n):
    divisors = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0 and 71 <= divisor <= 81:
            divisors += divisor
    return divisors