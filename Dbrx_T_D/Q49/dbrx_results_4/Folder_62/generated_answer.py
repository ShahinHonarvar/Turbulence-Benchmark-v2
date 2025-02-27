def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-08

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_number = fib(130)
    if decimal_integer % fib_number == 0:
        return True
    else:
        return False