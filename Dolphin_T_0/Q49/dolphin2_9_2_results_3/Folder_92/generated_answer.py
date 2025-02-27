def fibonacci(n):
    a, b = (0, 1)
    for i in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    return decimal % fibonacci(7) == 0