def if_decimal_is_divisible(binary_str):
    fib_74 = 1304969544928657
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_74 == 0