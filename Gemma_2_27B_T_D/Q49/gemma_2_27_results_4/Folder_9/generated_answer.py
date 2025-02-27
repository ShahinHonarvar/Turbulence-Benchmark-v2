def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_68 = 63245986
    return decimal_num % fib_68 == 0