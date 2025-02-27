def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_10 = 34
    return decimal % fib_10 == 0