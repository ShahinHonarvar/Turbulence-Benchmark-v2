def fib(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def binary_to_decimal(binary):
    return int(binary, 2)

def if_decimal_is_divisible(binary):
    decimal = binary_to_decimal(binary)
    fib_114 = fib(114)
    return decimal % fib_114 == 0