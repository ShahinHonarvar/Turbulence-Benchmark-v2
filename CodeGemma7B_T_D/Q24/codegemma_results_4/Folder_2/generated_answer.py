def sum_of_divisors_in_range(n):
    sum = 0
    for divisor in range(315, 956):
        if n % divisor == 0 and divisor >= 315 and (divisor <= 955):
            sum += divisor
    return sum or 0