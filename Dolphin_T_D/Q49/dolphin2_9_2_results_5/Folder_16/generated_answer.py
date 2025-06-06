def fibonacci(n):
    if n <= 1:
        return n
    a, b = (0, 1)
    for _ in range(2, n + 1):
        a, b = (b, a + b)
    return b

def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib = fibonacci(128)
    return decimal % fib == 0