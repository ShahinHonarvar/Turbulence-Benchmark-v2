def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_35 = 9227465
    return decimal_number % fib_35 == 0