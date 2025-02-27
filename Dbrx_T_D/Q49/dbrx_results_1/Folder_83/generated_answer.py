def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-08

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_representation):
    decimal_integer = binary_to_decimal(binary_representation)
    fib_number = 60
    while fib_number < 60 + 100:
        if is_fibonacci(fib_number) and decimal_integer % fib_number == 0:
            return True
        fib_number += 1
    return False