def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_114 = 2338744
    return decimal_integer % fib_114 == 0