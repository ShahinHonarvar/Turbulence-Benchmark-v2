def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_150 = 9.971931343963198e+30
    return decimal_number % fibonacci_150 == 0