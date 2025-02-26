def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_40 = 102334155
    return decimal % fib_40 == 0