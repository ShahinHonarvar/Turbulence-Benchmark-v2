def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_17th = 1597
    return decimal_number % fib_17th == 0