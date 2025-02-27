def if_decimal_is_divisible(binary_str):
    fib_27 = 196418
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_27 == 0