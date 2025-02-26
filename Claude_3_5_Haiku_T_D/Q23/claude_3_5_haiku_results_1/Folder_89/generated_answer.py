def find_divisors_in_range(n):
    return [divisor for divisor in range(14, 49) if n % divisor == 0]