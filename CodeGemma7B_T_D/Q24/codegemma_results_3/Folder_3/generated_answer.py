def sum_of_divisors_in_range(n):
    """Calculates the sum of divisors in a range."""
    divisor_sum = 0
    for i in range(43, 47):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum or 0