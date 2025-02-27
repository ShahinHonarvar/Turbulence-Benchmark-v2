import re

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b

def fibonacci_170th():
    fib_numbers = []
    a, b = (0, 1)
    while len(fib_numbers) < 170:
        fib_numbers.append(a)
        a, b = (b, a + b)
    return fib_numbers[-1]

def decimal_to_binary(n):
    return '{0:b}'.format(n)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_number = fibonacci_170th()
    return decimal_number % fib_number == 0