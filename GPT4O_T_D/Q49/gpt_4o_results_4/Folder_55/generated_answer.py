def if_decimal_is_divisible(binary_string):
    fib_39 = 39088169
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_39 == 0