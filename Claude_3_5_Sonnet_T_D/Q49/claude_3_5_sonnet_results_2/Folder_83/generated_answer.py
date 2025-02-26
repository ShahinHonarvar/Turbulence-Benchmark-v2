def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_60 = 1548008755920
    return decimal % fib_60 == 0