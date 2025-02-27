def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_56 = 225851433717
    return decimal_value % fib_56 == 0