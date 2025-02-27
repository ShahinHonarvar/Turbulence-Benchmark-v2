def if_decimal_is_divisible(binary_str: str) -> bool:
    decimal_num = int(binary_str, 2)
    fibonacci_num = fibonacci(139)
    return decimal_num % fibonacci_num == 0

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