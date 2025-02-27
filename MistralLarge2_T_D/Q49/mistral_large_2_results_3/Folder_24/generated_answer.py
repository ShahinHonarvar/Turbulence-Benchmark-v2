def if_decimal_is_divisible(binary_str):
    fib_56 = 350704366
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_56 == 0