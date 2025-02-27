def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib15 = 610
    return decimal % fib15 == 0