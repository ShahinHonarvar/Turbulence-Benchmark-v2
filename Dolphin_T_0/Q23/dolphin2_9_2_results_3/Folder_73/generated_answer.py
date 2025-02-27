def find_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return [d for d in divisors if d >= 46 and d <= 89]