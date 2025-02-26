def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_74 = 1304969544928657
    return decimal % fib_74 == 0