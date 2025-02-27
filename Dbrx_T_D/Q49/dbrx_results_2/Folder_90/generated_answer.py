def is_fibonacci(number):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(number - (phi ** number - psi ** number) / (phi - psi)) < 1e-10

def fibonacci_position(number):
    if number < 0:
        raise ValueError('Input must be non-negative')
    position = 0
    while True:
        if is_fibonacci(position) and (number % 2 ** position).bit_length() == 0:
            return position
        position += 1

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = fibonacci_position(decimal_integer)
    return fibonacci_number % 177 == 0 if fibonacci_number else False