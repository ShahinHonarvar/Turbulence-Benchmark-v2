def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_174 = 106270087479776000000000000000000000000000000000000000000000000000000000000000
    return decimal_number % fibonacci_174 == 0