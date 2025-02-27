def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_38 = 39088169
    return decimal_value % fib_38 == 0