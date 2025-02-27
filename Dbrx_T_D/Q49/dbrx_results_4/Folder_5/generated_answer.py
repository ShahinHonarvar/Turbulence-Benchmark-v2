def is_fibonacci(n):
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return abs(pow(phi, n) - pow(psi, n)) < 1.0 / (2 ** (n + 1) * sqrt_5)

def fibonacci():
    n = 0
    while True:
        if is_fibonacci(n):
            yield n
        n += 1

def fibonacci_85():
    fib = fibonacci()
    for _ in range(85):
        next(fib)
    return next(fib)

def decimal_from_binary(binary):
    return int(binary, 2)

def if_decimal_is_divisible(binary):
    decimal = decimal_from_binary(binary)
    return decimal % fibonacci_85() == 0