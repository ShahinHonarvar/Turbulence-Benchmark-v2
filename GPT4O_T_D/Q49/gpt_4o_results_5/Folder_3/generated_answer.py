def if_decimal_is_divisible(binary_string):
    fib_35 = 5702887
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_35 == 0