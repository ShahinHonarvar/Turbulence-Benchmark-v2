def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_84 = fibonacci_iterator()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
    return decimal_integer % fibonacci_84 == 0

def fibonacci_iterator():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)