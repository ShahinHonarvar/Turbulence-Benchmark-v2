def if_decimal_is_divisible(binary):
    fib_99 = fib(99)
    decimal = int(binary, 2)
    return decimal % fib_99 == 0

def fib(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a