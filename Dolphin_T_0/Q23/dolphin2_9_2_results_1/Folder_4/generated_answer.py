def find_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return [i for i in divisors if i >= 48 and i <= 60]