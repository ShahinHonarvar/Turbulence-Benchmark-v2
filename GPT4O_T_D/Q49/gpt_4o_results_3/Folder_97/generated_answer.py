def if_decimal_is_divisible(binary_str):
    fib_114 = 39088169
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_114 == 0