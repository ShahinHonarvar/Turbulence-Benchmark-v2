def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_138 = 363447532443
    return decimal % fib_138 == 0