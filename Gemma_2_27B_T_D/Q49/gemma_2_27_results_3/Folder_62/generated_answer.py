def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_130 = 38498462562917045013
    return decimal_number % fibonacci_130 == 0