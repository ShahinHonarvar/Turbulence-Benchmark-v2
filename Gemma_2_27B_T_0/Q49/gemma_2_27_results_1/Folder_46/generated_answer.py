def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_139 = 3596402737091
    return decimal_number % fibonacci_139 == 0