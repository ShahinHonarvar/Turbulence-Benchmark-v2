def if_decimal_is_divisible(binary_str):
    fib_66th = 27777890035288
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_66th == 0