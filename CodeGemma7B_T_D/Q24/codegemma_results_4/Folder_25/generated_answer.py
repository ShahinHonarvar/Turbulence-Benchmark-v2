def sum_of_divisors_in_range(n):
    if n == 1:
        return 0
    divisors = []
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    total_sum = 0
    for divisor in divisors:
        if divisor >= 84 and divisor <= 86:
            total_sum += divisor
    return total_sum