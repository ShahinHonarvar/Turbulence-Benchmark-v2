def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)
    fib_138 = fibonacci(138)
    return number % fib_138 == 0