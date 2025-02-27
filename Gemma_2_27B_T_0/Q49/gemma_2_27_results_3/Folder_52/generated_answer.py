def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_176 = 258402169773971
    return decimal_number % fibonacci_176 == 0