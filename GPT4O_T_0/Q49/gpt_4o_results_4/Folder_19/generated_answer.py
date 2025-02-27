def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_29 = 514229
    return decimal_number % fib_29 == 0