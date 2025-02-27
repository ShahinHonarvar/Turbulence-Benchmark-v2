def find_divisors_in_range(n):
    return [i for i in range(113, 991 + 1) if n % i == 0]