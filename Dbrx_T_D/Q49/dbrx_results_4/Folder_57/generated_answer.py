def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_80 = fibonacci_sequence()[-80]
    return decimal_integer % fibonacci_80 == 0

def fibonacci_sequence():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)