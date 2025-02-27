def sum_of_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    in_range = sum((d for d in divisors if 10 <= d <= 55))
    return in_range