def fib(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def binary_to_decimal(binary):
    decimal, i = (0, 0)
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def if_decimal_is_divisible(binary):
    decimal = binary_to_decimal(int(binary))
    fib_179 = fib(179)
    return decimal % fib_179 == 0