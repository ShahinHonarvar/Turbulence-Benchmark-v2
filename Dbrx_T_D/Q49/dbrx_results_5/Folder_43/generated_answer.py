def is_decimal_divisible_by_77th_fibonacci_number(binary_representation: str) -> bool:

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
    decimal_number = int(binary_representation, 2)
    return decimal_number % fibonacci(77) == 0