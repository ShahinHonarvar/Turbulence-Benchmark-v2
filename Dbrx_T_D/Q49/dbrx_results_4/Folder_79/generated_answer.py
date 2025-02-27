def if_decimal_is_divisible(binary_repr: str) -> bool:

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
    decimal_num = int(binary_repr, 2)
    fib_num = fibonacci(13)
    return decimal_num % fib_num == 0