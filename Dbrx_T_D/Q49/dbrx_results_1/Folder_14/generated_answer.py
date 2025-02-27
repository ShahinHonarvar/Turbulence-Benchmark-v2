def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fib_27 = fib(27)
    if decimal_integer % fib_27 == 0:
        return True
    else:
        return False

def fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n):
            a, b = (b, a + b)
        return b