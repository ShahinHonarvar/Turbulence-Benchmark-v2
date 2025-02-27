def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_78 = 8944394323791464
    return decimal_number % fib_78 == 0