def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_199 = fibonacci(199)
    return decimal % fib_199 == 0