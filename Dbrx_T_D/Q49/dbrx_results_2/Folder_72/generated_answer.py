def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = list(fibonacci())
    if len(fibonacci_numbers) < 175:
        raise ValueError('Not enough Fibonacci numbers generated')
    modulo_result = decimal_number % fibonacci_numbers[174]
    return modulo_result == 0