def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_67 = 44945570212853
    return decimal_number % fib_67 == 0