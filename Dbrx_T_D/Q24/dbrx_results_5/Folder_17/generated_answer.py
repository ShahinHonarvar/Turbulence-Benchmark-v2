def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for potential_divisor in range(1, n + 1):
        if n % potential_divisor == 0 and 10 <= potential_divisor <= 69:
            divisors_sum += potential_divisor
    return divisors_sum