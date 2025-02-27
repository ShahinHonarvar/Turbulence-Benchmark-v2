def sum_of_divisors_in_range(n):
    divisors = [i for i in range(71, 82) if i % n == 0]
    return sum(divisors) if divisors else 0