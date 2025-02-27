def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_ninth = 34
    return decimal_integer % fib_ninth == 0