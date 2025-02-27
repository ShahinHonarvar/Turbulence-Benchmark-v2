def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / 5 ** 0.5) < 1e-10

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal = to_decimal(binary_string)
    for _ in range(153):
        next(fibonacci())
    return decimal % next(fibonacci()) == 0