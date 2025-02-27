def if_decimal_is_divisible(binary_string):
    fib_114 = 14028366653498915298923761
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_114 == 0