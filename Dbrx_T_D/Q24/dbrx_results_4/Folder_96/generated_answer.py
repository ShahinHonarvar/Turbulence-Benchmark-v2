def sum_of_divisors_in_range(n):
    divisors = sum((i for i in range(5, 10) if n % i == 0 and i <= n))
    return divisors