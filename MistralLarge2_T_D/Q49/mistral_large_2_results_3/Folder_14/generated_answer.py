def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_27 = 196418
    return decimal % fib_27 == 0