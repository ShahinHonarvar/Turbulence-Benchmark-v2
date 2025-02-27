def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-08

def fibonacci():
    current, next = (0, 1)
    while True:
        yield current
        current, next = (next, current + next)

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_numbers = set()
    for i, fib in enumerate(fibonacci()):
        if i == 135:
            break
        fibonacci_numbers.add(fib)
    return decimal_integer % min(fibonacci_numbers) == 0