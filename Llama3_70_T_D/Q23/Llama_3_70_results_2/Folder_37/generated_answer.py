def find_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return []
    return [i for i in range(3, 8) if n % i == 0]