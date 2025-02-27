def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_49 = 7778742049
    return decimal_number % fib_49 == 0