def if_decimal_is_divisible(binary_str):
    fib_48 = 4807526976
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_48 == 0