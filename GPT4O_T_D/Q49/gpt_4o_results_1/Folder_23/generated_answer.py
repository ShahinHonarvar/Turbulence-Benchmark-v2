def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_48 = 4807526976
    return decimal_number % fib_48 == 0