def if_decimal_is_divisible(binary_representation: str) -> bool:

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = list(fibonacci())
    if len(fibonacci_sequence) < 95:
        raise ValueError('The Fibonacci sequence is not long enough')
    return decimal_integer % fibonacci_sequence[94] == 0