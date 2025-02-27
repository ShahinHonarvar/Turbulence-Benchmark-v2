def if_decimal_is_divisible(binary_string):
    fib_15th = 377
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_15th == 0