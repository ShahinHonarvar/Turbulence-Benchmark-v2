def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / 5 ** 0.5) < 1e-10

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if is_fibonacci(decimal_integer):
        fib_number = next(fibonacci())
        for _ in range(196):
            fib_number = next(fibonacci())
        return decimal_integer % fib_number == 0
    else:
        return False