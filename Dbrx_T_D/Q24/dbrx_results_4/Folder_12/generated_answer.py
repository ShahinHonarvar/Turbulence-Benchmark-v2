def sum_of_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0 and 13 <= d <= 62]
    return sum(divisors) if divisors else 0