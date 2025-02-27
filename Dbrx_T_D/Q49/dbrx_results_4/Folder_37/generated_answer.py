def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-10

def fibonacci():
    n = 0
    while True:
        yield n
        n += 1

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    for i, fib in enumerate(fibonacci()):
        if fib >= 46:
            break
        if decimal_integer % fib == 0:
            return True
    return False if n == 0 else is_fibonacci(n)