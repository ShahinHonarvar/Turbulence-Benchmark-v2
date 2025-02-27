import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def find_Fibonacci_no(k):
    i = 0
    temp = fibonacci(i)
    while temp < k:
        i += 1
        temp = fibonacci(i)
    return temp

def if_decimal_is_divisible(binary_representation):
    integer_value = int(binary_representation, 2)
    i = 0
    temp = fibonacci(i)
    while temp < integer_value:
        i += 1
        temp = fibonacci(i)
    return temp % integer_value == 0