def if_decimal_is_divisible(binary_rep: str) -> bool:

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
    decimal_num = int(binary_rep, 2)
    return decimal_num % fibonacci(24) == 0