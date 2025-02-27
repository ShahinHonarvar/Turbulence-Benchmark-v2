def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_64 = fib(64)
    return decimal_integer % fibonacci_64 == 0

def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n):
            a, b = (b, a + b)
        return b