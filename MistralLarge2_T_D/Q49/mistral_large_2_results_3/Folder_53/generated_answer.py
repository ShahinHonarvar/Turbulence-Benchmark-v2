def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_64 = fibonacci(64)
    return decimal_value % fib_64 == 0