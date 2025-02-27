def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_9th = 21
    return decimal % fib_9th == 0