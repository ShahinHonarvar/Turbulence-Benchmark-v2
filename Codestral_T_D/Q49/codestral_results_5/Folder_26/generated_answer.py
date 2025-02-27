def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_138 = fibonacci(138)
    return decimal % fib_138 == 0