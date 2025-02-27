def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_66 = 135544064625
    return decimal_number % fibonacci_66 == 0