def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_185 = 10946197
    return decimal % fib_185 == 0