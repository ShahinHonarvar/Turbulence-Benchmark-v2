def if_decimal_is_divisible(binary: str) -> bool:

    def fib(n):
        if n in (1, 2):
            return 1
        return fib(n - 1) + fib(n - 2)
    decimal = 0
    for bit in reversed(binary):
        decimal *= 2
        decimal |= int(bit)
    for n in range(50):
        if decimal % fib(166 + n) == 0:
            return True
    return False