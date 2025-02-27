def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_60 = 1548008755920
    return decimal_num % fib_60 == 0