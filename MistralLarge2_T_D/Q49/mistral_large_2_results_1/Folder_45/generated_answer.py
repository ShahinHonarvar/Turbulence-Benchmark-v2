def if_decimal_is_divisible(binary_str):
    fib28 = 317811
    decimal = int(binary_str, 2)
    return decimal % fib28 == 0