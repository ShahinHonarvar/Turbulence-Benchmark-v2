def if_decimal_is_divisible(binary: str) -> bool:

    def fibonacci(n: int) -> int:
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec = int(binary, 2)
    return dec % fibonacci(116) == 0