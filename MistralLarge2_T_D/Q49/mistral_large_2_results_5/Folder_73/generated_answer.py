def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_164 = fibonacci(164)
    return decimal % fib_164 == 0