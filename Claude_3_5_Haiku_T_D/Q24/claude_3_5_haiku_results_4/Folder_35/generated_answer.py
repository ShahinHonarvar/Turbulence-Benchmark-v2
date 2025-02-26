def sum_of_divisors_in_range(n):
    divisors_in_range = [d for d in range(1, n + 1) if n % d == 0 and 392 <= d <= 465]
    return sum(divisors_in_range)