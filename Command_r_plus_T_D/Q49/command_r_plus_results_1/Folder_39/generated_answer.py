def if_decimal_is_divisible(binary_str):
    fib_15th = 610
    decimal = int(binary_str, 2)
    return decimal % fib_15th == 0