def fib(n):
    a, b = (0, 1)
    while n > 0:
        a, b = (b, a + b)
        n -= 1
    return a

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_180 = fib(180)
    return decimal % fib_180 == 0