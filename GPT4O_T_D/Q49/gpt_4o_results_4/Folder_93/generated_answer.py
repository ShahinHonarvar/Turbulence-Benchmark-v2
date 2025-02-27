def if_decimal_is_divisible(binary_string):
    fib_number_59 = 956722026041
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_number_59 == 0