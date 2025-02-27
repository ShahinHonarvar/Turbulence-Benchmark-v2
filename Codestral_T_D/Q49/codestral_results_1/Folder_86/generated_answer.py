def if_decimal_is_divisible(binary: str) -> bool:

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary):
        return int(binary, 2)
    dec = binary_to_decimal(binary)
    fib_135 = fib(135)
    return dec % fib_135 == 0