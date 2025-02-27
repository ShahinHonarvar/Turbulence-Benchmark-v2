def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal_integer = binary_to_decimal(binary_string)
    fifty_fourth_fibonacci = next(filter(is_fibonacci, itertools.count(0, 54)))
    return decimal_integer % fifty_fourth_fibonacci == 0