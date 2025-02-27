def is_fibonacci(n):
    return (5 * n * n - 4) % 10 == 0 or (5 * n * n + 4) % 10 == 0

def fibonacci_n(n):
    fib_n = 0
    a, b = (0, 1)
    for _ in range(n - 1):
        a, b = (b, a + b)
    fib_n = b
    return fib_n

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_num = fibonacci_n(29)
    return decimal_num % fib_num == 0