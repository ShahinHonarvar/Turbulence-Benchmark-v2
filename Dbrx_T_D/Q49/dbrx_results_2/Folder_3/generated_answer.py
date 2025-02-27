def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-08

def decimal_from_binary(bstring):
    return int(bstring, 2)

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(bstring):
    decimal = decimal_from_binary(bstring)
    fib = fibonacci()
    for _ in range(35):
        if decimal % next(fib) == 0:
            return True
    return False