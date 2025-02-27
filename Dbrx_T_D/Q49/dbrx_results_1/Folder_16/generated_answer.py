def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = fibonacci(128)
    if decimal_number % fibonacci_number == 0:
        return True
    else:
        return False

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