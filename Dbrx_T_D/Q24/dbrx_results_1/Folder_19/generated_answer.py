def sum_of_divisors_in_range(n):
    divisors = [d for d in range(1, min(n, 8)) if n % d == 0]
    return sum(divisors)