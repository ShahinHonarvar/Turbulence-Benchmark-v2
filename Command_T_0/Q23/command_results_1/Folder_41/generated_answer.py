def find_divisors_in_range(n):
    return [i for i in range(2, n + 1) if n % i == 0]