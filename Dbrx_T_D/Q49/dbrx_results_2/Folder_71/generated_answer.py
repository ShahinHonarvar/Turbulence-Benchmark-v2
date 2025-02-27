from itertools import islice

def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = next(islice(fibonacci(), 147, 147), None)
    return True if fibonacci_number and decimal_number % fibonacci_number == 0 else False

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)