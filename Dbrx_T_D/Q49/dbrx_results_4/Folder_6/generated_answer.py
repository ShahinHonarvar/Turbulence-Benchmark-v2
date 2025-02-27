def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fibonacci_index(n):
    phi = (1 + 5 ** 0.5) / 2
    return int(round((phi * n + 0.5) / (phi ** 2 + 1)))

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if decimal_integer % 2 == 0:
        fibonacci_number = fibonacci_index(decimal_integer // 2)
    else:
        fibonacci_number = fibonacci_index((decimal_integer - 1) // 2) + 1
    return fibonacci_number % 233 == 0