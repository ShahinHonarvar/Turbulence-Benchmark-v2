import math

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def is_fib(n):
    return int((5 * n ** 2 + 4) ** 0.5) % 4 == 0

def binary_to_decimal(binary_string):
    decimal = 0
    binary_string = str(binary_string)[::-1]
    for index, digit in enumerate(binary_string):
        if digit == '1':
            decimal += 2 ** index
    return decimal

def if_decimal_is_divisible(binary_representation):
    index = 0
    while True:
        decimal = binary_to_decimal(binary_representation)
        if is_fib(index + 188):
            if decimal % fib(index + 188) == 0:
                return True
        binary_representation = str(int(binary_representation, 2) + 1)
        index += 1