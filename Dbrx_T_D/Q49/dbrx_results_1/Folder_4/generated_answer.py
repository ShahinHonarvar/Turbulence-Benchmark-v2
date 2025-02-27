def is_fibonacci(number):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(number - (phi ** number - psi ** number) / 5 ** 0.5) < 1e-10

def fibonacci_index(n):
    phi = (1 + 5 ** 0.5) / 2
    return round(1 / 5 ** 0.5 * log(n * 5 ** 0.5) / log(phi))

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if not is_fibonacci(fibonacci_index(decimal_integer)):
        return False
    return decimal_integer % fibonacci_sequence(118) == 0

def fibonacci_sequence(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers