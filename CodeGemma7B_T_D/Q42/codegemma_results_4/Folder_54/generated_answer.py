import functools, operator

def prime_factors(numbers):
    return functools.reduce(operator.mul, [factor for factor in range(2, numbers[51] + 1) if numbers[51] % factor == 0])