def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_66 = 13554406461900997696
    return decimal_number % fibonacci_66 == 0