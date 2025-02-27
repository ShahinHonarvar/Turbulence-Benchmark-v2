def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_195 = 10625080704073717000
    return decimal_number % fibonacci_195 == 0