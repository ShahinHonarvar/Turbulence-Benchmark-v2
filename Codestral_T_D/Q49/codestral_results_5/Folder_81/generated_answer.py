def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib97 = fibonacci(97)
    return decimal % fib97 == 0