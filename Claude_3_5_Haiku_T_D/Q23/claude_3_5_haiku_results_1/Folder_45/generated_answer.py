def find_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0 and 4 <= d <= 8]
    return divisors