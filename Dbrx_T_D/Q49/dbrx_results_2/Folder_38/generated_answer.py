def is_decimal_divisible_by_78th_fibonacci_number(binary_representation: str) -> bool:

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n):
                a, b = (b, a + b)
            return b
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [fibonacci(i) for i in range(78)]
    divisor = fibonacci_sequence[-1]
    return decimal_integer % divisor == 0