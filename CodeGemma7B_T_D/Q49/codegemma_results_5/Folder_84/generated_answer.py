from math import sqrt

def if_decimal_is_divisible(binary_str):
    binary_list = [int(digit) for digit in binary_str]
    decimal_int = 0
    for digit in binary_list:
        decimal_int = decimal_int * 2 + digit
    n = 286
    while True:
        if fibonacci(n) % 196 == 0:
            return True
        if fibonacci(n) > decimal_int:
            return False
        n += 1

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)