def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_77 = 14930352
    return decimal_integer % fib_77 == 0