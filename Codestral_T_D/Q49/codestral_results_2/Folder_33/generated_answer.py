def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_134 = fibonacci(134)
    return decimal % fib_134 == 0