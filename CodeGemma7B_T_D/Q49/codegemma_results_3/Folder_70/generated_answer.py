from math import sqrt

def if_decimal_is_divisible(binary):
    if binary == '0':
        return False
    decimal = int(binary, 2)
    if decimal == 0:
        return False
    fib_prev_prev = 0
    fib_prev = 1
    fib_current = fib_prev_prev + fib_prev
    fib_count = 2
    while fib_count < 137:
        fib_prev_prev = fib_prev
        fib_prev = fib_current
        fib_current = fib_prev_prev + fib_prev
        fib_count += 1
    if decimal % fib_current == 0:
        return True
    else:
        return False