def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_13 = 233
    return decimal % fib_13 == 0