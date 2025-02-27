def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_4th = 3
    return decimal % fib_4th == 0