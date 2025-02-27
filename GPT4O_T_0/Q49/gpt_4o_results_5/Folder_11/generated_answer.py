def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_16th = 987
    return decimal_number % fib_16th == 0