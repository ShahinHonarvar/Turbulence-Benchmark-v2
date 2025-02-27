def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_10th = 34
    return decimal_number % fib_10th == 0