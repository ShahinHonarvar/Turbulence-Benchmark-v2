def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_29 = 317811
    return decimal_number % fib_29 == 0