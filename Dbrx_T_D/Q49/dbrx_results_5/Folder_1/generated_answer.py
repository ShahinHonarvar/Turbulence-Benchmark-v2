def if_decimal_is_divisible(binary_representation: str) -> bool:

    def fibonacci(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                c = a + b
                a, b = (b, c)
            return c
    decimal_integer = int(binary_representation, 2)
    ninetieth_fibonacci = fibonacci(90)
    return decimal_integer % ninetieth_fibonacci == 0