import itertools

def is_fibonacci(n):
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return abs(n - (phi ** n / sqrt_5 - psi ** n / sqrt_5)) < 1e-10

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def fib_at_least_until(n):
    return list(itertools.islice(fibonacci(), n + 1))

def fibonacci_number_divisible_by_94():
    fib_numbers = fib_at_least_until(1000)
    return next((x for x in fib_numbers if is_fibonacci(x) and x % 94 == 0))

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci_number_divisible_by_94() == 0