def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_78 = 8944394323791464
    return decimal % fib_78 == 0