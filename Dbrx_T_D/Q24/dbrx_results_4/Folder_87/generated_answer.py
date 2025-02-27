def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for divisor in range(1, n + 1):
        if n % divisor != 0:
            continue
        if 50 <= divisor <= 81:
            divisors_sum += divisor
    return divisors_sum