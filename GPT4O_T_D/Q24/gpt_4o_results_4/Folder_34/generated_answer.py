def sum_of_divisors_in_range(n):
    divisors_range = range(4, 6)
    total_sum = sum((d for d in divisors_range if n % d == 0))
    return total_sum