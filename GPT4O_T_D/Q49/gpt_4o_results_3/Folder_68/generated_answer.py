def if_decimal_is_divisible(binary_str):
    fib_38 = 39088169
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_38 == 0