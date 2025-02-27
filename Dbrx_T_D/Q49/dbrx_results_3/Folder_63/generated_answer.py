def is_fibonacci_number_divisible_by_144(binary_representation: str) -> bool:

    def fibonacci(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n):
                a, b = (b, a + b)
            return b
    decimal_number = int(binary_representation, 2)
    fib_number = fibonacci(144)
    return decimal_number % fib_number == 0