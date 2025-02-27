def is_decimal_divisible_by_fibonacci(n: str) -> bool:

    def fibonacci(sequence_length: int) -> int:
        if sequence_length <= 0:
            return 0
        elif sequence_length == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, sequence_length):
                a, b = (b, a + b)
            return b
    decimal = int(n, 2)
    fibonacci_number = fibonacci(56)
    return decimal % fibonacci_number == 0