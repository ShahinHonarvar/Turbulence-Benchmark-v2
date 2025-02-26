def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_115 = 9227465
    return decimal_value % fib_115 == 0