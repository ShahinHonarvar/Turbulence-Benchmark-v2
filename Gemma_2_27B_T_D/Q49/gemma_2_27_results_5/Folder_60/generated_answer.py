def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_108 = 7091506067561111607
    return decimal_number % fibonacci_108 == 0