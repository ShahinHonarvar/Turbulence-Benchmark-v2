from functools import reduce

def sum_of_divisors(n):
    return reduce(lambda a, b: a + (n % b < 1) * b, range(1, int(n ** 0.5) + 1), 0)

def sum_of_divisors_in_range(n):
    divisors = sum_of_divisors(n)
    return 0 if divisors < 14 or divisors > 93 else divisors