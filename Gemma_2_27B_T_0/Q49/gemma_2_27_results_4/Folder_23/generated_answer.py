def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_48 = 4807526976
    return decimal_number % fibonacci_48 == 0