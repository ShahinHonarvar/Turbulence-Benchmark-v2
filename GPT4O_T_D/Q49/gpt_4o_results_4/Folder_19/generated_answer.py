def if_decimal_is_divisible(binary_representation):
    fib_number_29 = 317811
    decimal_number = int(binary_representation, 2)
    return decimal_number % fib_number_29 == 0