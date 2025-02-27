def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_166 = fibonacci(166)
    return decimal % fib_166 == 0