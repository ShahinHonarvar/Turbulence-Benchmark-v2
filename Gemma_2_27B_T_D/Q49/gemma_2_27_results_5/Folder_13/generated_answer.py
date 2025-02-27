def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_174 = 18642037800
    return decimal % fibonacci_174 == 0