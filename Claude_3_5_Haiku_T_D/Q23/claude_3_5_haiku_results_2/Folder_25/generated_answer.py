def find_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0 and 84 <= d <= 86]
    return divisors