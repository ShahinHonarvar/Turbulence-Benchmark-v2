def if_decimal_is_divisible(binary_rep):
    decimal_value = int(binary_rep, 2)
    fib_29 = 514229
    return decimal_value % fib_29 == 0