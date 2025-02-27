def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_77 = 552793970088475721
    return decimal_number % fibonacci_77 == 0