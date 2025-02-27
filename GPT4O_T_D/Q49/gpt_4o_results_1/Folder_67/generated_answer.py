def if_decimal_is_divisible(binary_string):
    fib_107 = 306171383
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_107 == 0