def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib39 = 63245986
    return decimal % fib39 == 0