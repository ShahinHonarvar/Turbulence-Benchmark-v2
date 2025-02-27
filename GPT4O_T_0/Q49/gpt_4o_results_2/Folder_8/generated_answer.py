def if_decimal_is_divisible(binary_str):
    fib_54 = 86267571272
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_54 == 0