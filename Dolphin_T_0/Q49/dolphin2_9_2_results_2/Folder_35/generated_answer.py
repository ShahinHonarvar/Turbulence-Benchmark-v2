def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_187 = fib(187)
    return decimal % fib_187 == 0