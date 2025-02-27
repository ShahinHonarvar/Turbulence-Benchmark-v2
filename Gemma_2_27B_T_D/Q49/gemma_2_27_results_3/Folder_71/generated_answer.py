def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_147 = 1107566917973
    return decimal_number % fibonacci_147 == 0