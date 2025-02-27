def if_decimal_is_divisible(binary_str):
    fib_90 = 2880067194370816120
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_90 == 0