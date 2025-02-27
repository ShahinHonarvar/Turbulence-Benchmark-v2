from decimal import Decimal

def dec_value(b):
    value = Decimal(0)
    for i, j in enumerate(b):
        value += Decimal(j) * Decimal(2 ** (len(b) - i - 1))
    return value

def fibonacci(n):
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

def if_decimal_is_divisible(b):
    b = b.replace('0b', '')
    return int(dec_value(b)) % fibonacci(146) == 0