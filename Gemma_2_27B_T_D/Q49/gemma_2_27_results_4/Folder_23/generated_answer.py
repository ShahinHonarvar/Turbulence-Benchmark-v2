def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_48 = 4807526976
    return decimal % fib_48 == 0