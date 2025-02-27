def sum_of_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    divisors_in_range = [d for d in divisors if 70 <= d <= 72]
    return sum(divisors_in_range) if divisors_in_range else 0