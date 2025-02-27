def if_decimal_is_divisible(binary_string):
    fib_19th = 4181
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_19th == 0