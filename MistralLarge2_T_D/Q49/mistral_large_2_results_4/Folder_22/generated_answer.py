def if_decimal_is_divisible(binary_string):
    fib_20th = 4181
    decimal = int(binary_string, 2)
    return decimal % fib_20th == 0