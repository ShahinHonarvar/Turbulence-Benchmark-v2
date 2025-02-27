def if_decimal_is_divisible(binary_str):
    fib_69 = 117669030460994
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_69 == 0