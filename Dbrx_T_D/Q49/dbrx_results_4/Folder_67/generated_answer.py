def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-08

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_number = next(filter(is_fibonacci, count(0, 0.1)))
    return decimal_integer % fib_number == 0