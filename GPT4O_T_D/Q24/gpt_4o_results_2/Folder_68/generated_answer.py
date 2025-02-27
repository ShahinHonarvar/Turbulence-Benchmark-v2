def sum_of_divisors_in_range(n):
    return sum((d for d in range(3, 7) if n % d == 0))