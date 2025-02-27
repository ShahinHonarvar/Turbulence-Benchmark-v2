from itertools import islice

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = next(islice(fibonacci(), 45, 46))
    return decimal_number % fibonacci_number == 0