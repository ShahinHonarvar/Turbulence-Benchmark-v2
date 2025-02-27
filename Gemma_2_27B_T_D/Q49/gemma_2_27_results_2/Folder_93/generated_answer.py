def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_59 = 577834467327114
    return decimal_integer % fib_59 == 0