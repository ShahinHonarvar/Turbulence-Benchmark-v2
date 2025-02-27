def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-08

def fibonacci():
    n = 0
    while True:
        if is_fibonacci(n):
            yield n
        n += 1

def to_decimal(binary):
    return int(binary, 2)

def if_decimal_is_divisible(binary):
    decimal = to_decimal(binary)
    for i, fib in enumerate(fibonacci()):
        if fib == 105:
            if decimal % fib == 0:
                return True
            else:
                return False