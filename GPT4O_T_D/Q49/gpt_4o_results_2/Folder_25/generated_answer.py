def if_decimal_is_divisible(binary_string):
    fib_19 = 4181
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_19 == 0