def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_27 = 196418
    return decimal_number % fib_27 == 0