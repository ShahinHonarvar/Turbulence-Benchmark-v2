def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_178 = 116089462731446931213574715686
    return decimal % fibonacci_178 == 0