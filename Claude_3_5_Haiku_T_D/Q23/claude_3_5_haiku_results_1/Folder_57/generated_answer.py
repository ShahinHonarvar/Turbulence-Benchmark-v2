def find_divisors_in_range(n):
    divisors = [d for d in range(15, 93) if n % d == 0]
    return divisors