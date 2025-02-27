def sum_of_divisors_in_range(n):
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    return sum((div for div in divisors if 120 <= div <= 349))