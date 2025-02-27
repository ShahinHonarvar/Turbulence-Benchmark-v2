def fibonacci(n: int) -> int:
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(s: str) -> bool:
    n = int(s, 2)
    return n % fibonacci(160) == 0