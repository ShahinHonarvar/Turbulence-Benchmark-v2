def find_divisors_in_range(n):
    divisors = [d for d in range(3, 5) if n % d == 0]
    return divisors