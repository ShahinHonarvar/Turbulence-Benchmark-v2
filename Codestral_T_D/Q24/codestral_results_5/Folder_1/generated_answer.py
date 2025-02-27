def sum_of_divisors_in_range(n):
    return sum((i for i in range(10, min(n, 55) + 1) if n % i == 0))