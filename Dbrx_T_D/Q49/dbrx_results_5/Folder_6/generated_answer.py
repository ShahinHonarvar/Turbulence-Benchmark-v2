def if_decimal_is_divisible(bin_str: str) -> bool:

    def fibonacci(divisor: int) -> int:
        a, b = (0, 1)
        for _ in range(divisor - 1):
            a, b = (b, a + b)
        return b
    decimal = int(bin_str, 2)
    return decimal % fibonacci(185) == 0