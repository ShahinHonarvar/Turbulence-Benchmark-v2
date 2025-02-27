def if_decimal_is_divisible(binary_str):
    fib_n_24 = 28657
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_n_24 == 0