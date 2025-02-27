def fib(n):
    if n <= 1:
        return n
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_108 = fib(108)
    return decimal % fib_108 == 0