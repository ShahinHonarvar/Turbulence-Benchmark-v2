def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_90th = 2880067194370816120
    return decimal % fib_90th == 0