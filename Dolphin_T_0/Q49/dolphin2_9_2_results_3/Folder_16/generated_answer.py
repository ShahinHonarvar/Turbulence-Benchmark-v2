def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def decimal_from_binary(s):
    return int(s, 2)

def if_decimal_is_divisible(binary):
    fib_128 = fibonacci(128)
    decimal = decimal_from_binary(binary)
    return decimal % fib_128 == 0