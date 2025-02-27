def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_str):
    fib_178 = fibonacci(178)
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_178 == 0