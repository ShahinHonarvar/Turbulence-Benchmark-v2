def if_decimal_is_divisible(binary_str):
    fib_13th = 233
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_13th == 0