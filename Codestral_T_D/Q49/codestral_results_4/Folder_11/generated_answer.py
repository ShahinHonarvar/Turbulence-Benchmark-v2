def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_16 = fibonacci(16)
    return decimal % fib_16 == 0