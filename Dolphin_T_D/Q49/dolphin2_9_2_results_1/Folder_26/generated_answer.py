def if_decimal_is_divisible(binary_decimal_string):
    binary_decimal = int(binary_decimal_string, 2)
    fib137 = 0
    fib138 = 1
    i = 138
    while i > 0:
        fib137, fib138 = (fib138, fib137 + fib138)
        i -= 1
    return binary_decimal % fib138 == 0