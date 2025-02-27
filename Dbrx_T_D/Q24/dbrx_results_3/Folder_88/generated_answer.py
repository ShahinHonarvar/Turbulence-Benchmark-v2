def sum_of_divisors_in_range(n):
    divisors = filter(lambda x: x > 0 and 6 <= x <= 7, range(1, n + 1))
    return sum(divisors) if divisors else 0