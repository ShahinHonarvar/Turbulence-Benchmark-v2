def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = list(fibonacci())
    if len(fibonacci_numbers) < 166:
        raise ValueError('Not enough Fibonacci numbers generated')
    return decimal_number % fibonacci_numbers[165] == 0