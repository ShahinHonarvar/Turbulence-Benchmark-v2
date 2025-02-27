def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = next(filter(lambda x: x > decimal_number, (fib() for _ in range(178))))
    return decimal_number % fibonacci_number == 0

def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)