def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fibonacci():
    current, next = (0, 1)
    while True:
        yield current
        current, next = (next, current + next)

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fib_sequence = fibonacci()
    for _ in range(179):
        fib_number = next(fib_sequence)
    return decimal_integer % fib_number == 0