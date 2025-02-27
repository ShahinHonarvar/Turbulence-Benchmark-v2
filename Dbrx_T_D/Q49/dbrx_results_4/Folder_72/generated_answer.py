def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(n - (phi ** n - psi ** n) / (phi - psi)) < 1e-10

def fibonacci_index(n):
    phi = (1 + 5 ** 0.5) / 2
    return int(round(1 / phi * (n * phi ** 2)))

def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number_to_check = fibonacci_index(175)
    if fibonacci_number(fibonacci_number_to_check) == 0:
        return False
    if decimal_number % fibonacci_number(fibonacci_number_to_check) == 0:
        return True
    else:
        return False