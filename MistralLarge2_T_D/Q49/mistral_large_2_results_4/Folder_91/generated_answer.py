def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_sixth = 5
    return decimal % fib_sixth == 0