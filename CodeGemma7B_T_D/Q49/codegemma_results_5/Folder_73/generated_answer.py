import math

def if_decimal_is_divisible(binary_representation):
    counter = 0
    fib = 0
    fib_count = 0
    sqrt_length = int(math.sqrt(len(binary_representation)))
    while fib_count < sqrt_length:
        fib_count += 1
        fib = fibonacci(fib_count)
    divisible_by_fib = True
    for digit in reversed(binary_representation[:sqrt_length]):
        if digit == '1':
            counter += fib
        divisible_by_fib = divisible_by_fib and counter % fib == 0
    return divisible_by_fib

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)