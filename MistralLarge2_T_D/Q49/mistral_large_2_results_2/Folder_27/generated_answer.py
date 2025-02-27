def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_87 = 135720777
    return decimal % fib_87 == 0