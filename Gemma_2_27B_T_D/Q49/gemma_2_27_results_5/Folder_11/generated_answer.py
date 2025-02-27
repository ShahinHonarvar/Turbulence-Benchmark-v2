def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib16 = 987
    return decimal % fib16 == 0